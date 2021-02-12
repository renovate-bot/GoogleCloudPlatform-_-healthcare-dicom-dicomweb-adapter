import os
import random
import string

ERROR_CODE = 1

def runCommand(command, message):
    result = os.system(command)
    print(message, result)
    return result

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Store name is:", result_str)
    return result_str

# get short SHA from env
def get_short_sha():
   return os.environ.get("SHORT_SHA")

# get imageproject from env
def get_imageproject():
   return os.environ.get("IMAGEPROJECT")

# clear data
def clear_data():
    return runCommand("rm -R dcm4che", "remove dcm4che")

# install environment
def install_environment():
    return runCommand("./integration_test/scripts/install-env.sh", "install environment exit with")

# clone-dcm4che
def clone_dcm4che():
    return runCommand("git clone https://github.com/dcm4che/dcm4che.git dcm4che", "clone-dcm4che exit with")

# checkout-dcm4che-tag
def checkout_dcm4che_tag():
    return runCommand("cd dcm4che && git checkout \"tags/5.15.1\"", "checkout-dcm4che-tag exit with")

# build-tools
def build_tools():
    return runCommand("./integration_test/scripts/mvn-install-tools.sh", "build-tools exit with")

# store-scp
def store_scp(store_csp_run_step, store_scp_port):
    return runCommand("./integration_test/scripts/run-store-scp-and-wait.sh " + store_csp_run_step + " "+store_scp_port, "store-scp exit with")

# build adapter
def build_adapter():
    return runCommand("./integration_test/scripts/build-adapters.sh", "build adapter exit with")

# build adapter image
def build_adapter_image(imageproject, short_sha):
    return runCommand("./integration_test/scripts/build-adapter-image.sh "+imageproject+" "+short_sha, "build adapter image exit with")

# setup-dataset-and-dicom-store
def setup_dataset_and_dicom_store(project, location, dataset, store_name):
    return runCommand("./integration_test/scripts/setup-dataset-and-store.sh "+project+" "+location+" "+dataset+" "+store_name, "setup-dataset-and-dicom-store exit with")

# run import adapter
def run_import_adapter(adapter_port, version, project, location, dataset, store_name, store_scp_run_step, store_scp_port, com_scu_step, com_scu_port):
    return runCommand("./integration_test/scripts/run-import-adapter.sh "+adapter_port+" "+version+" "+project+" "+location+" "+dataset+" "+store_name+" "+store_scp_run_step+" "+store_scp_port+" "+com_scu_step+" "+com_scu_port, "run import adapter exit with")


# run import adapter with http2 mode
def run_import_adapter_http2(adapter_port, version, project, location, dataset, store_name):
    return runCommand("./integration_test/scripts/run-import-adapter-http2.sh "+adapter_port+" "+version+" "+project+" "+location+" "+dataset+" "+store_name, "run import adapter exit with")

# run import adapter with local backup mode
def run_import_adapter_local_backup(adapter_port, version, project, location, dataset, store_name):
    return runCommand("./integration_test/scripts/run-import-adapter-local-backup.sh "+adapter_port+" "+version+" "+project+" "+location+" "+dataset+" "+store_name, "run import adapter exit with")

# run import adapter with gsc backup mode
def run_import_adapter_gcs_backup(adapter_port, version, project, location, dataset, store_name, bucket):
    return runCommand("./integration_test/scripts/run-import-adapter-gcs-backup.sh "+adapter_port+" "+version+" "+project+" "+location+" "+dataset+" "+store_name+" "+bucket, "run import adapter exit with")

# wait-for-adapter
# wait-for-storescp
def wait_for_port(host, port):
    return runCommand("./integration_test/scripts/wait-for-port.sh "+host+" " + port, "wait-for-adapter exit with")

# run-store-scu
def run_store_scu(host, adapter_port, file_path):
    return runCommand("export PATH=/opt/apache-maven-3.6.3/bin:$PATH &&"
           "cd dcm4che/dcm4che-tool/dcm4che-tool-storescu &&"
           "mvn -ntp exec:java -Dexec.mainClass=org.dcm4che3.tool.storescu.StoreSCU -Dexec.args=-\"c IMPORTADAPTER@"+host+":"+adapter_port+" "+file_path+"\"", "run-store-scu exit with")

# run-find-scu-instance
def run_find_scu_instance(host, adapter_port):
    return runCommand("export PATH=/opt/apache-maven-3.6.3/bin:$PATH &&"
           "cd /workspace/dcm4che/dcm4che-tool/dcm4che-tool-findscu &&"
           "mvn -ntp  exec:java -Dexec.mainClass=org.dcm4che3.tool.findscu.FindSCU -Dexec.args=\"-c IMPORTADAPTER@"+host+":"+adapter_port+" -L IMAGE -X --out-cat --out-file findscu-instance-result.xml --out-dir ../../../integration_test/\"", "run-find-scu-instance exit with")

# run-find-scu-series
def run_find_scu_series(host, adapter_port):
    return runCommand("export PATH=/opt/apache-maven-3.6.3/bin:$PATH &&"
           "cd /workspace/dcm4che/dcm4che-tool/dcm4che-tool-findscu &&"
           "mvn -ntp  exec:java -Dexec.mainClass=org.dcm4che3.tool.findscu.FindSCU -Dexec.args=\"-c IMPORTADAPTER@"+host+":"+adapter_port+" -L SERIES -X --out-cat --out-file findscu-series-result.xml --out-dir ../../../integration_test/\"", "run-find-scu-series exit with")

# run-find-scu-study
def run_find_scu_study(host, adapter_port):
    return runCommand("export PATH=/opt/apache-maven-3.6.3/bin:$PATH &&"
           "cd /workspace/dcm4che/dcm4che-tool/dcm4che-tool-findscu &&"
           "mvn -ntp  exec:java -Dexec.mainClass=org.dcm4che3.tool.findscu.FindSCU -Dexec.args=\"-c IMPORTADAPTER@"+host+":"+adapter_port+" -L STUDY -X --out-cat --out-file findscu-study-result.xml --out-dir ../../../integration_test/\"", "run-find-scu-study exit with")

# run-move-scu
def run_move_scu(host, adapter_port):
    return runCommand("export PATH=/opt/apache-maven-3.6.3/bin:$PATH &&"
           "cd /workspace/dcm4che/dcm4che-tool/dcm4che-tool-movescu &&"
           "mvn -ntp  exec:java -Dexec.mainClass=org.dcm4che3.tool.movescu.MoveSCU -Dexec.args=\"-c IMPORTADAPTER@"+host+":"+adapter_port+" --dest STORESCP\"", "run-move-scu exit with")

# run-commitment-scu
def run_commitment_scu(host, adapter_port, com_scu_port, file_path):
    return runCommand("export PATH=/opt/apache-maven-3.6.3/bin:$PATH &&"
           "cd /workspace/dcm4che/dcm4che-tool/dcm4che-tool-stgcmtscu &&"
           "mvn -ntp  exec:java -Dexec.mainClass=org.dcm4che3.tool.stgcmtscu.StgCmtSCU -Dexec.args=\"-c IMPORTADAPTER@"+host+":"+adapter_port+" -b STGCMTSCU:"+com_scu_port+" --explicit-vr --directory /workspace/integration_test/commitment_result "+file_path+"\"", "run-commitment-scu exit with")

# check-store-curl
def check_store_curl(version, project, location, dataset, store_name, replaced_uid, file_path):
    return runCommand("integration_test/scripts/curl-dcm.sh https://healthcare.googleapis.com/"+version+"/projects/"+project+"/locations/"+location+"/datasets/"+dataset+"/dicomStores/"+store_name+"/dicomWeb/studies/"+replaced_uid+"/series/"+replaced_uid+"/instances/"+replaced_uid+" "+file_path, "check-store-curl exit with")

# check diff
def check_diff(file_path1, file_path2):
    return runCommand("diff "+file_path1+" "+file_path2, "check-diff exit with")

# check-commitment-diff
def check_commitment_diff():
    return runCommand("chmod -R 777 dcm4che/dcm4che-tool/dcm4che-tool-dcm2xml &&"
           "cd dcm4che/dcm4che-tool/dcm4che-tool-dcm2xml &&"
           "/workspace/integration_test/scripts/diff-commitment-result.sh", "check-commitment-diff exit with")

# delete-dicom-store
def delete_dicom_store(store_name, project, dataset, location):
    return runCommand("gcloud beta healthcare dicom-stores delete "+store_name+" --project="+project+" --dataset="+dataset+" --location="+location+" --quiet", "delete-dicom-store "+store_name+" exit with")

# verify script result
def verify_result(result):
    if result != 0:
        exit(ERROR_CODE)

# change permission
def change_permission():
    return runCommand("chmod -R 777 /workspace/integration_test/scripts", "grant permission exit with")
