#include <stdio.h>
#include <netdb.h>
#include <arpa/inet.h>

int main(int argc, char *argv[]){
	int my_con;
	int con;
	int port=0;
	int ports=65525;
	struct sockaddr_in target;
	
	if (argc < 2){
		printf("|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| \n");
		printf("|-|           PortScan          |-| \n");
		printf("|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| \n");
		printf("Uses: %s + ip_address\n",argv[0]);
		printf("Ex: %s 192.168.0.1 \n",argv[0]);
		return 0;
	}else{
		for (port=0;port<ports;port++){
			my_con = socket(AF_INET, SOCK_STREAM, 0);
			target.sin_family = AF_INET;
			target.sin_port = htons(port);
			target.sin_addr.s_addr = inet_addr(argv[1]);
			con = connect(my_con, (struct sockaddr *)&target, sizeof target);
       	
			if (con == 0){
				printf("Port [%d] Open! \n",port);
				close(my_con);
				close(con);
			}else{
				close(my_con);
				close(con);
			}
		}
		printf("Scan finished! \n");
		return 0;
	}
}
