# import paramiko
import asyncssh
import time
import asyncio


async def sshTest(ipaddress, deviceUsername, devicePassword, sshPort):  # finalDict
    try:
        print("Performing SSH Connection to the device")
        # client = paramiko.SSHClient()
        # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # client.connect(ipaddress, username=deviceUsername, password=devicePassword, port=sshPort, look_for_keys=False, allow_agent=False)
        async with  asyncssh.connect(ipaddress, username=deviceUsername, password=devicePassword,
                                     known_hosts=None) as conn:
            async with conn.start_sftp_client() as sftp:
                # Here you can enter the commands you want to execute, e.g. import data from a device
                await sftp.get("folder_device", "folder_local", preserve=True, recurse=True)

        print("Channel established")
    except Exception as e:
        print(e)


async def main():
    start = time.time()

    ip_list = ['192.168.254.11', '192.168.255.11']
    tasks = []
    for ip in ip_list:
        tasks.append(asyncio.create_task(sshTest(ip, 'admin', 'admin', '22')))
    await asyncio.gather(*tasks)

    end = time.time()
    print("The time of execution of above program is :", end - start)


if __name__ == "__main__":
    asyncio.run(main())
