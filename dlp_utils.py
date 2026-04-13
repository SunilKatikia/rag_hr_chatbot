from google.cloud import dlp_v2
from secret_manager import config

def mask_pii_global(text):
    dlp = dlp_v2.DlpServiceClient()
    parent = f"projects/{config.project_id}/locations/global"
    
    info_types = [
        {"name": "PERSON_NAME"}, {"name": "EMAIL_ADDRESS"},
        {"name": "PHONE_NUMBER"}, {"name": "PASSPORT"}
    ]
    
    inspect_config = {"info_types": info_types}
    deidentify_config = {
        "info_type_transformations": {
            "transformations": [{
                "primitive_transformation": {"character_mask_config": {"masking_character": "*"}}
            }]
        }
    }
    
    response = dlp.deidentify_content(
        request={
            "parent": parent,
            "deidentify_config": deidentify_config,
            "inspect_config": inspect_config,
            "item": {"value": text},
        }
    )
    return response.item.value
