#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<openssl/sha.h>

int main()
{
	unsigned char final[20] = {0};
	unsigned int text[4] = {0};

	char tomatch[] = "\xff\xe5";
	int p = 2;

	for(int i =0;i<0xffffffff;i++)
	{
		for(int j =0;j<0xffffffff;j++)
		{
			for(int k =0;k<0xffffffff;k++)
			{
				for(int l=0;l<0xffffffff;l++)
				{
					text[0] = i;
					text[1] = j;
					text[2] = k;
					text[3] = l;
					SHA1((const unsigned char *)text,16,final);

					if(!memcmp(tomatch,final,p))
					{
						printf("Input : ");
						for(int m=0;m<16;m++)
							printf("%02x",((unsigned char*)text)[m]);
						printf("\n");
						printf("Output : ");
						for(int m =0;m<20;m++)
							printf("%02x",final[m]);
						printf("\n");
						exit(0);
					}
				}
				puts("4");
			}
			puts("3");
		}
		puts("2");
	}
	puts("1");
	return 0;
}
