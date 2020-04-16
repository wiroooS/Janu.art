#include <stdio.h>
#include <iostream>


int main (){
ulang:
	system("cls");
	int j,i,b,k,baris,min,max;
			printf("Tabel Perkalian\n");
			printf("##################\n\n");
				printf("Masukkan nilai a = ");
				scanf("%d",&j);
				printf("\nMasukkan nilai b = ");
				scanf("%d",&i);
				printf("\n");
				for(baris=1;baris<=j;baris++){
					printf("    %d",baris);
				}
				printf("\n");
				for(b=1;b<=j;b++){
					printf("\n%d",b);
					
						for(k=1;k<=i;k++){
							printf("   %d ",b*k);
							}
				printf("\n\n");
			}
			
			min=1;
			max=(i*j);
			
			printf("Nilai Minimum = %d",min);
			printf("\nNilai Maksimum = %d",max);

	return 0;		
}
