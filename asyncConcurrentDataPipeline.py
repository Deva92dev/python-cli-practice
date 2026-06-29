import json
from enum import Enum
from jsonschema import ValidationError
import asyncio
import aiofiles


customer_file_path = (
    r"C:\Users\acer\Desktop\AI ML Ideas Build\Python Practice\Basics\customers.json"
)
product_file_path = (
    r"C:\Users\acer\Desktop\AI ML Ideas Build\Python Practice\Basics\products.json"
)
order_file_path = (
    r"C:\Users\acer\Desktop\AI ML Ideas Build\Python Practice\Basics\orders.json"
)
summary_file_path_json = (
    r"C:\Users\acer\Desktop\AI ML Ideas Build\Python Practice\Basics\summary.json"
)
summary_file_path_csv = (
    r"C:\Users\acer\Desktop\AI ML Ideas Build\Python Practice\Basics\summary.csv"
)


def log_execution(func):
    def inner(*args):
        print("decorator is started running")
        func(*args)
        print("decorator stopped running")

    return inner


class Dataset_Type(Enum):
    CUSTOMER = "customers"
    PRODUCT = "products"
    ORDER = "orders"


class DataValidator:
    def __init__(self):
        self.schemas = {
            "customers": {
                "type": "object",
                "properties": {
                    "customer_id": {"type": "integer"},
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "city": {"type": "string"},
                },
                "required": ["customer_id", "name", "email", "city"],
            },
            "products": {
                "properties": {
                    "product_id": {"type": "integer"},
                    "name": {"type": "string"},
                    "category": {"type": "string"},
                    "price": {"type": "integer"},
                    "stock": {"type": "number"},
                },
                "required": ["product_id", "name", "category", "price", "stock"],
            },
            "orders": {
                "type": "object",
                "properties": {
                    "order_id": {"type": "integer"},
                    "customer_id": {"type": "integer"},
                    "product_id": {"type": "integer"},
                    "quantity": {"type": "number"},
                    "order_date": {"type": "string"},
                    "status": {"type": "string"},
                },
                "required": [
                    "order_id",
                    "customer_id",
                    "product_id",
                    "quantity",
                    "order_date",
                    "status",
                ],
            },
        }


class Dataset:
    generic_path = ""

    def __init__(self, dataset_type: Dataset_Type):
        self.data = None
        self.dataset_type = dataset_type
        self.results = None

    async def load_dataset(self):
        if self.dataset_type.value == "customers":
            self.generic_path = customer_file_path
        elif self.dataset_type.value == "products":
            self.generic_path = product_file_path
        elif self.dataset_type.value == "orders":
            self.generic_path = order_file_path

        try:
            async with aiofiles.open(self.generic_path, "r") as file:
                contents = await file.read()
                self.data = json.loads(contents)
        except (json.JSONDecodeError, FileNotFoundError):
            self.data = []

        return self.data

    def validate_dataset(self, dataset_type):
        # add more if needed
        missing_keys = []
        empty_values = 0
        error_count = 0
        seen_ids = set()
        required_keys = []
        duplicates = 0
        duplicates_count = []
        invalid_records = {
            "record": [],
            "dataset": self.dataset_type.value,
            "reason": [],
        }
        valid_records = []

        validator = DataValidator()
        if self.dataset_type.value not in validator.schemas:
            raise ValueError(f"Unknown Dataset type: {dataset_type}")

        if isinstance(self.data, list):
            data = self.data

        for key, each in validator.schemas[dataset_type].items():
            if isinstance(each, list):
                required_keys = each

        try:
            for each in data:
                for key in required_keys:
                    if key not in each:
                        missing_keys.append(each)
                        error_count += 1

                _, first_value = next(iter(each.items()))
                if first_value not in seen_ids:
                    seen_ids.add(first_value)
                else:
                    duplicates += 1
                    duplicates_count.append(first_value)

                for _, each_value in each.items():
                    if each_value == "":
                        empty_values += 1

                if self.dataset_type.value == "customers":
                    if each.get("email"):
                        if "@" not in each.get("email", ""):
                            invalid_records["record"].append(each)
                            reason = "email schema failed"
                            invalid_records["reason"].append(reason)
                            continue

                    if each.get("customer_id"):
                        if not 1 <= each.get("customer_id") <= 100:
                            invalid_records["record"].append(each)
                            reason = "customer_id is out of range"
                            invalid_records["reason"].append(reason)
                            continue

                valid_records.append(each)

                if self.dataset_type.value == "products":
                    if each.get("price"):
                        if not each.get("price") > 0:
                            invalid_records["record"].append(each)
                            reason = "price can not be lower than 0"
                            invalid_records["reason"].append(reason)
                            continue

                    if each.get("stock"):
                        if not each.get("stock") > 0:
                            invalid_records["record"].append(each)
                            reason = "stock can not be lower than 0"
                            invalid_records["reason"].append(reason)
                            continue

                if self.dataset_type.value == "orders":
                    if each.get("quantity"):
                        if not each.get("quantity") > 0:
                            invalid_records["record"].append(each)
                            reason = "quantity can not be lower than 0"
                            invalid_records["reason"].append(reason)
                            continue

            self.results = {
                "dataset": self.dataset_type.value,
                "total_data": len(data),
                "missing_values": len(missing_keys),
                "empty_values": empty_values,
                "total_errors": error_count,
                "duplicates": duplicates_count,
                "valid_record": len(data) - error_count,
                "invalid_record": invalid_records["record"],
            }

            if self.dataset_type.value == "products":
                most_common_category = []
                prices = 0
                for every in data:
                    category = every["category"]
                    most_common_category.append(category)

                    prices += every["price"]
                    average_price = prices / len(data)

                    counts = {}
                    for each in most_common_category:
                        counts[each] = counts.get(each, 0) + 1

                maximum = max(counts, key=lambda k: counts[k])
                self.results["average_price"] = average_price
                self.results["most_common_category"] = maximum

            return self.results

        except ValidationError as e:
            print(f"Validation failed for {self.dataset_type}: {e.message}")
            return None

    @log_execution
    def generate_invalid_records(self):
        if self.results:
            invalids = self.results["invalid_record"]
            generating = (each for each in invalids)

            for every in generating:
                print(every)


class DatasetManager:
    async def process_datasets(self, dataset):
        await dataset.load_dataset()

        await asyncio.to_thread(
            dataset.validate_dataset,
            dataset.dataset_type.value,
        )

        return {
            "dataset": dataset.dataset_type.value,
            "results": dataset.results,
        }


def flatten_dict(d, parent_key="", sep="_"):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            # Flatten lists by indexing them
            for i, item in enumerate(v):
                list_key = f"{new_key}{sep}{i}"
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, list_key, sep=sep).items())
                else:
                    items.append((list_key, item))
        else:
            items.append((new_key, v))

    return dict(items)


def flatten_list_of_dicts(result, sep="_"):
    return [flatten_dict(d, sep=sep) for d in result]


class ReportExporter:
    async def export_report_to_csv(self, result, filepath):
        flattened = [flatten_dict(record) for record in result]
        fieldnames = set()
        for row in flattened:
            fieldnames.update(row.keys())

        fieldnames = sorted(fieldnames)

        async with aiofiles.open(
            filepath, mode="w", newline="", encoding="utf-8"
        ) as file:
            await file.write(",".join(fieldnames) + "\n")
            # Write every row
            for row in flattened:
                values = []
                for field in fieldnames:
                    value = row.get(field, "")
                    # CSV cannot directly store lists/dicts so convert them into JSON strings.
                    if isinstance(value, (dict, list)):
                        value = json.dumps(value)
                    values.append(str(value))
                await file.write(",".join(values) + "\n")

        return flattened

    async def export_report_to_json(self, results, filepath):
        async with aiofiles.open(filepath, "w", encoding="utf-8") as file:
            await file.write(
                json.dumps(
                    results,
                    indent=4,
                    ensure_ascii=False,
                )
            )

        return results


def main():
    customer_dataset = Dataset(Dataset_Type.CUSTOMER)
    product_dataset = Dataset(Dataset_Type.PRODUCT)
    order_dataset = Dataset(Dataset_Type.ORDER)

    manager = DatasetManager()
    report = ReportExporter()

    async def concurrent():
        return await asyncio.gather(
            manager.process_datasets(customer_dataset),
            manager.process_datasets(product_dataset),
            manager.process_datasets(order_dataset),
        )

    results = asyncio.run(concurrent())

    async def summary():
        await report.export_report_to_json(
            results,
            summary_file_path_json,
        )

        await report.export_report_to_csv(
            results,
            summary_file_path_csv,
        )

    asyncio.run(summary())

    summaries = asyncio.run(summary())
    print("from exporter: ", summaries)
    # flattened = flatten_list_of_dicts(results)
    # for item in flattened:
    #     print(item)

    # customer_dataset.generate_invalid_records()
    # product_dataset.generate_invalid_records()
    # order_dataset.generate_invalid_records()


if __name__ == "__main__":
    main()
