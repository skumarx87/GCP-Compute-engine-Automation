from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

ComputeEngine = get_driver(Provider.GCE)
# Note that the 'PEM file' argument can either be the JSON format or
# the P12 format.
driver = ComputeEngine('libcloud@ferrous-weaver-249914.iam.gserviceaccount.com','/home/sathish/gcp_pem.json',
                       project='ferrous-weaver-249914')

#(driver.list_images())

### Function to findout the gcp image name to provide arg in create instance function ###

def list_all_gcp_images(driver):
        images = driver.list_images()
        for image in images:
                print(image)

### use below function to create compute instance ##

def create_instance(driver):
        s = 'n1-standard-1'
        i = 'centos-7-v20191121'
        z = 'us-central1-a'

        sa_scopes = [{'email': 'default','scopes': ['storage-ro']}]
        node_1 = driver.create_node("n2", s, i, z, ex_service_accounts=sa_scopes)

create_instance(driver)
list_all_gcp_images(driver)
