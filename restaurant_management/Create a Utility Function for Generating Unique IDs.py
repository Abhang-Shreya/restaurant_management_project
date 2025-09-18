import uuid

def generate_unique_id(prefix=''):
    return f"{prefix}{uuid.uuid4().hex[:10]}"

from utils.id_utils import generate_unique_id
print(generate_unique_id('ORD_'))  # e.g. ORD_a3f5c9d2e1
