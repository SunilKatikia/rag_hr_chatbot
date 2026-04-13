from google.cloud import secretmanager

class Config:
    def __init__(self):
        self.client = secretmanager.SecretManagerServiceClient()
        self.project_id = self._get_secret("GCP_PROJECT_ID")
        # Multi-region or Global settings
        self.location = "us-central1" 
        self.dataset_id = "global_hr_data"
        self.table_id = "hr_policy_chunks"

    def _get_secret(self, secret_id):
        name = f"projects/your-project-id/secrets/{secret_id}/versions/latest"
        response = self.client.access_secret_version(request={"name": name})
        return response.payload.data.decode("UTF-8")

config = Config()
