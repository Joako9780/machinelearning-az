# Plantilla de Pre Procesado de Datos en R
# Importar el Dataset 

dataset = read.csv("Data.csv")

# Tratamiento de los valores NA
# con $ se accede a un valor del dataframe
# dataset$Age es un vector
# funcion ifelse() para evaluar la condicion de NA en algun valor
# del dataset y calcular la media o dejar el valor original segun la condicion
# funcion is.na() evalua si un dato es NA
# ave() produce un subconjunto de x a partir de las observaciones realizadas
# na.rm NA Remove, o sea sin los valores NA
# FUN ahora es una funcion que calcula la media de los x sin tener en cuenta
# los valores NA

dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Salary)

# Codificar variables categoricas

# conversion de variables categoricas a factores
# c() es la sintaxis de vector en R, en Python es con []

dataset$Country = factor(dataset$Country,
                         levels = c("France", "Germany", "Spain"),
                         labels = c(0, 1, 2))

dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No", "Yes"),
                           labels = c(0, 1))



