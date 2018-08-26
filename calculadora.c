#include <stdio.h>
#include <stdlib.h>

int main(){

int num1, num2, result, operacao;

do

printf("Bem vindo a Agecalc\n");
printf("Porfavor escolha umas das operacoes abaixo\n");
printf("\n1 Soma, 2 Subtracao, 3 Divisão, 4 Multipicacao\n");

scanf("%d", &operacao);
switch (operacao){
  case 1:
    printf("\nVoce esta na area de soma!\n");
    printf("\nDigite o primeiro numero para somar: ");
    scanf("%d", &num1);
    printf("\nDigite o segundo numero para somar: ");
    scanf("%d", &num2);
    result = num1 + num2;
    printf("\nO resultado da soma e: %d\n", result);
    printf("Digite 00 para voltar ao inicio\n" );
    scanf("%d", &operacao);
  default:
    printf("Voce nao escolheu uma opcao valida\n" );

}

  return 0;
}
