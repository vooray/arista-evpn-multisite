from nornir import InitNornir
from nornir_netmiko import netmiko_send_config
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Task, Result


def task_send_config(task: Task) -> Result:
    return Result(
        host = task.host,
        result=task.run(
            netmiko_send_config, config_file=task.host.data["config_file"],
        )
    )

if __name__=="__main__":
    nr = InitNornir(config_file="config.yaml")

    result = nr.run(task=task_send_config)
    print_result(result)

