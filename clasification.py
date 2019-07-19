import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

df = pd.read_csv('encuesta_internautas_cluster_k_5_medias.csv', delimiter=',')
X = df.values
print(df.shape)
print(df.groupby('cluster').size())

feature_names = ["tiene_telefono_fijo","tiene_computadora","usa_computadora_como_herramienta_trabajo","usa_computadora_musica_videos","usa_computadora_juegos","usa_computadora_internet","usa_computadora_estudio","mira_noticias_tv","mira_deportes_tv","mira_salud_educacion_tv","mira_entretenimiento_tv","tiene_tv_cable","tiene_tv_satelital","tiene_radio","usa_internet_contactar_amigos","usa_internet_buscar_info","usa_internet_para_trabajo","usa_celular_sms","usa_celular_musica","usa_celular_videos","usa_celular_juegos","usa_celular_conect_internet","usa_celular_fotos","usa_internet_cel_contactar_amigos","usa_internet_cel_buscar_info","usa_internet_cel_fin_academico","usa_internet_cel_trabajo","usa_internet_cel_ver_noticias","usa_internet_cel_descargar_archivos","usa_internet_cel_jugar","usa_internet_cel_musica_video","usa_internet_cel_rrss","usa_internet_cel_correo_electr","busca_noticias_internet","busca_ciencia_tecnologia_internet","busca_entretenimiento_internet","busca_info_educativa_interent","trabajo_alguna_vez","trabajo_relacionado_tecnologias","realizo_compra_por_internet","consulta_movimientos_bancarios","usa_facebook","usa_twitter","usa_whatsapp","usa_instagram","usa_youtube","usa_rrss_conocer_gente","usa_rrss_temas_politicos","usa_rrss_noticias","usa_rrss_compartir_contenido","usa_rrss_videos_fotos","apoyo_causa_social_rrss","pertenece_grupo_o_comunidad","realizo_llamada_voz_internet","sexo","tiene_alcantarillado","tiene_lavadora","tiene_microondas","tiene_calefon","tiene_tarjeta_credto","tiene_casa_propia","tiene_automovil_reciente","dias_uso_computadora_semana = 3","dias_uso_computadora_semana = 5","dias_uso_computadora_semana = 0","dias_uso_computadora_semana = 7","dias_uso_computadora_semana = 6","dias_uso_computadora_semana = 2","dias_uso_computadora_semana = 4","dias_uso_computadora_semana = 1","tiene_internet_fijo = 3","tiene_internet_fijo = 1","tiene_internet_fijo = 0","prepago_postpago = 1","prepago_postpago = 2","prepago_postpago = 0","empresa_telco = 2","empresa_telco = 3","empresa_telco = 1","so_celular = 1","so_celular = 2","so_celular = 4","dias_uso_internet_semana = 7","dias_uso_internet_semana = 5","dias_uso_internet_semana = 3","dias_uso_internet_semana = 1","dias_uso_internet_semana = 4","dias_uso_internet_semana = 6","dias_uso_internet_semana = 2","nivel_uso_internet_para_trabajo = 1","nivel_uso_internet_para_trabajo = 0","nivel_uso_internet_para_trabajo = 3","nivel_uso_internet_para_trabajo = 2","prefiere_medio_para_noticias_nacionales = 2","prefiere_medio_para_noticias_nacionales = 5","prefiere_medio_para_noticias_nacionales = 1","prefiere_medio_para_noticias_nacionales = 4","prefiere_medio_para_noticias_nacionales = 3","prefiere_medio_para_noticias_nacionales = 6","prefiere_medio_para_noticias_nacionales = 7","prefiere_medio_para_noticias_internacionales = 5","prefiere_medio_para_noticias_internacionales = 1","prefiere_medio_para_noticias_internacionales = 3","prefiere_medio_para_noticias_internacionales = 4","prefiere_medio_para_noticias_internacionales = 2","prefiere_medio_para_noticias_internacionales = 6","prefiere_medio_ciencia_tecnologia = 1","prefiere_medio_ciencia_tecnologia = 5","prefiere_medio_ciencia_tecnologia = 4","prefiere_medio_ciencia_tecnologia = 6","prefiere_medio_ciencia_tecnologia = 2","prefiere_medio_ciencia_tecnologia = 3","prefiere_medio_ciencia_tecnologia = 7","prefiere_medio_para_entretenimiento = 1","prefiere_medio_para_entretenimiento = 5","prefiere_medio_para_entretenimiento = 3","prefiere_medio_para_entretenimiento = 7","prefiere_medio_para_entretenimiento = 6","prefiere_medio_para_entretenimiento = 4","prefiere_medio_para_entretenimiento = 2","prefiere_medio_para_ofertas_laborales = 1","prefiere_medio_para_ofertas_laborales = 5","prefiere_medio_para_ofertas_laborales = 3","prefiere_medio_para_ofertas_laborales = 4","prefiere_medio_para_ofertas_laborales = 2","prefiere_medio_para_ofertas_laborales = 7","prefiere_medio_para_ofertas_laborales = 6","cree_medio_rapido = 2","cree_medio_rapido = 1","cree_medio_rapido = 6","cree_medio_rapido = 5","cree_medio_rapido = 3","cree_medio_rapido = 4","cree_medio_rapido = 7","cree_medio_veridico = 1","cree_medio_veridico = 3","cree_medio_veridico = 4","cree_medio_veridico = 5","cree_medio_veridico = 2","cree_medio_veridico = 7","cree_medio_veridico = 6","cree_medio_serio = 1","cree_medio_serio = 3","cree_medio_serio = 5","cree_medio_serio = 4","cree_medio_serio = 2","cree_medio_serio = 7","cree_medio_serio = 6","cree_medio_claro = 1","cree_medio_claro = 3","cree_medio_claro = 5","cree_medio_claro = 4","cree_medio_claro = 7","cree_medio_claro = 2","cree_medio_claro = 6","cree_medio_imparcial = 2","cree_medio_imparcial = 1","cree_medio_imparcial = 3","cree_medio_imparcial = 4","cree_medio_imparcial = 6","cree_medio_imparcial = 5","cree_medio_imparcial = 7","cree_medio_profundo = 1","cree_medio_profundo = 3","cree_medio_profundo = 5","cree_medio_profundo = 4","cree_medio_profundo = 6","cree_medio_profundo = 2","cree_medio_profundo = 7","cree_medio_participativo = 2","cree_medio_participativo = 6","cree_medio_participativo = 1","cree_medio_participativo = 5","cree_medio_participativo = 4","cree_medio_participativo = 3","cree_medio_participativo = 7","nivel_instruccion = 4","nivel_instruccion = 3","nivel_instruccion = 6","nivel_instruccion = 8","nivel_instruccion = 7","nivel_instruccion = 2","nivel_instruccion = 5","nivel_instruccion = 1","estado_civil = 2","estado_civil = 1","estado_civil = 3","estado_civil = 4","primer_idioma = 1","categoria_ocupacional = 4","categoria_ocupacional = 1","categoria_ocupacional = 3","categoria_ocupacional = 6","categoria_ocupacional = 2","categoria_ocupacional = 9","categoria_ocupacional = 5","categoria_ocupacional = 8","categoria_ocupacional = 7","nivel_instruccion_jefe_hogar = 7","nivel_instruccion_jefe_hogar = 1","nivel_instruccion_jefe_hogar = 4","nivel_instruccion_jefe_hogar = 8","nivel_instruccion_jefe_hogar = 2","nivel_instruccion_jefe_hogar = 5","nivel_instruccion_jefe_hogar = 3","nivel_instruccion_jefe_hogar = 6","estabilidad_laboral_jefe_hogar = 1","estabilidad_laboral_jefe_hogar = 2","estabilidad_laboral_jefe_hogar = 4","estabilidad_laboral_jefe_hogar = 5","estabilidad_laboral_jefe_hogar = 3","ingreso_mensual_prom_hogar = 3","ingreso_mensual_prom_hogar = 1","ingreso_mensual_prom_hogar = 4","ingreso_mensual_prom_hogar = 6","ingreso_mensual_prom_hogar = 5","ingreso_mensual_prom_hogar = 2","departamento = 1","departamento = 4","departamento = 6","departamento = 3","departamento = 5","departamento = 7","departamento = 8","departamento = 9","departamento = 2","tipo_localidad = 1","tipo_localidad = 2","tipo_localidad = 3","gasto_mes_telco_out = range1 [-∞ - 36.500]","gasto_mes_telco_out = range2 [36.500 - 72.500]","gasto_mes_telco_out = range3 [72.500 - 122.500]","gasto_mes_telco_out = range4 [122.500 - ∞]","pago_internet_mes_out = 0-50","pago_internet_mes_out = 51-100","pago_internet_mes_out = 101-150","pago_internet_mes_out = 150-inf","cant_personas_convive = 0-3","cant_personas_convive = 4-6","cant_personas_convive = 6-inf","cant_banios = 0-2","cant_banios = 3-5","cant_dias_usa_rrss = 0-2","cant_dias_usa_rrss = 3-4","cant_dias_usa_rrss = 4-7","edad = 0-18","edad = 18-25","edad = 25-35","edad = 35-45","edad = 45-inf","edad_uso_computadora_primera_vez = 0-18","edad_uso_computadora_primera_vez = 18-25","edad_uso_computadora_primera_vez = 25-35","edad_uso_computadora_primera_vez = 35-45"]
X = df[feature_names]
y = df['cluster']

log_cols=["Classifier", "Accuracy"]
log = pd.DataFrame(columns=log_cols)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
print(X_train.shape)
print(X_test.shape)

# Logistic regresion
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
print('Accuracy of Logistic regression classifier on training set: {:.2f}'
     .format(logreg.score(X_train, y_train)))
print('Accuracy of Logistic regression classifier on test set: {:.2f}'
     .format(logreg.score(X_test, y_test)))

log_entry = pd.DataFrame([['LogReg', logreg.score(X_test, y_test)*100]], columns=log_cols)
log = log.append(log_entry)

pred = logreg.predict(X_test)
print("Confution matrix")
print(confusion_matrix(y_test, pred))
print("Classification report")
print(classification_report(y_test, pred))
print("="*20)

# Decision tree
clf = DecisionTreeClassifier().fit(X_train, y_train)
print('Accuracy of Decision Tree classifier on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))
print('Accuracy of Decision Tree classifier on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))
log_entry = pd.DataFrame([['Decision tree', clf.score(X_test, y_test)*100]], columns=log_cols)
log = log.append(log_entry)

pred = clf.predict(X_test)
print("Confution matrix")
print(confusion_matrix(y_test, pred))
print("Classification report")
print(classification_report(y_test, pred))
print("="*20)

# LDA
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)
print('Accuracy of LDA classifier on training set: {:.2f}'
     .format(lda.score(X_train, y_train)))
print('Accuracy of LDA classifier on test set: {:.2f}'
     .format(lda.score(X_test, y_test)))
log_entry = pd.DataFrame([['LDA', lda.score(X_test, y_test)*100]], columns=log_cols)
log = log.append(log_entry)

pred = lda.predict(X_test)
print("Confution matrix")
print(confusion_matrix(y_test, pred))
print("Classification report")
print(classification_report(y_test, pred))
print("="*20)

# KNN
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print('Accuracy of K-NN classifier on training set: {:.2f}'
     .format(knn.score(X_train, y_train)))
print('Accuracy of K-NN classifier on test set: {:.2f}'
     .format(knn.score(X_test, y_test)))
log_entry = pd.DataFrame([['KNN', knn.score(X_test, y_test)*100]], columns=log_cols)
log = log.append(log_entry)

pred = knn.predict(X_test)
print("Confution matrix")
print(confusion_matrix(y_test, pred))
print("Classification report")
print(classification_report(y_test, pred))
print("="*20)

# Naive Bayes
gnb = GaussianNB()
gnb.fit(X_train, y_train)
print('Accuracy of GNB classifier on training set: {:.2f}'
     .format(gnb.score(X_train, y_train)))
print('Accuracy of GNB classifier on test set: {:.2f}'
     .format(gnb.score(X_test, y_test)))
log_entry = pd.DataFrame([['Naive Bayes', gnb.score(X_test, y_test)*100]], columns=log_cols)
log = log.append(log_entry)

pred = gnb.predict(X_test)
print("Confution matrix")
print(confusion_matrix(y_test, pred))
print("Classification report")
print(classification_report(y_test, pred))
print("="*20)

# SVM
svm = SVC()
svm.fit(X_train, y_train)
print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(X_test, y_test)))
log_entry = pd.DataFrame([['SVM', svm.score(X_test, y_test)*100]], columns=log_cols)
log = log.append(log_entry)
pred = svm.predict(X_test)
print(classification_report(y_test, pred))

pred = svm.predict(X_test)
print("Confution matrix")
print(confusion_matrix(y_test, pred))
print("Classification report")
print(classification_report(y_test, pred))
print("="*20)

# Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)  
rf.fit(X_train, y_train)
print('Accuracy of RF classifier on training set: {:.2f}'
     .format(rf.score(X_train, y_train)))
print('Accuracy of RF classifier on test set: {:.2f}'
     .format(rf.score(X_test, y_test)))
log_entry = pd.DataFrame([['RF', rf.score(X_test, y_test)*100]], columns=log_cols)
log = log.append(log_entry)

pred = rf.predict(X_test)
print("Confution matrix")
print(confusion_matrix(y_test, pred))
print("Classification report")
print(classification_report(y_test, pred))
print("="*20)

# Neural network
nn = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)  
nn.fit(X_train, y_train)
print('Accuracy of NN classifier on training set: {:.2f}'
     .format(nn.score(X_train, y_train)))
print('Accuracy of NN classifier on test set: {:.2f}'
     .format(nn.score(X_test, y_test)))
log_entry = pd.DataFrame([['NEURAL NETWORK', nn.score(X_test, y_test)*100]], columns=log_cols)
log = log.append(log_entry)

pred = nn.predict(X_test)
print("Confution matrix")
print(confusion_matrix(y_test, pred))
print("Classification report")
print(classification_report(y_test, pred))
print("="*20)

# # XGBoost
# xgboost = XGBClassifier()  
# xgboost.fit(X_train, y_train)
# print('Accuracy of XGBoost classifier on training set: {:.2f}'
#      .format(xgboost.score(X_train, y_train)))
# print('Accuracy of XGBoost classifier on test set: {:.2f}'
#      .format(xgboost.score(X_test, y_test)))

# sns.set_color_codes("muted")
# sns.barplot(x='Accuracy', y='Classifier', data=log, color="b")

# plt.xlabel('Accuracy %')
# plt.title('Classifier Accuracy')
# plt.show()

# print(log)