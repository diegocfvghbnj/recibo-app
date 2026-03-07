# ---------------------------
# BASE DE DATOS 
# ---------------------------

##  "SKU": {"nombre": "Producto A", "publico": 100.0, "25": 75.0, "50": 50.0},

productos = {
    # BATIDOS 
    "030K": {"nombre": "Herbalife #1 Arroz con leche", "publico": 934.00, "25": 727.26, "35": 644.75, "42": 586.99, "50": 520.98},
    "049K": {"nombre": "Herbalife #1 Coco", "publico": 934.00, "25": 727.26, "35": 644.75, "42": 586.99, "50": 520.98},
    "0884": {"nombre": "Herbalife #1 Choco avellana", "publico": 934.00, "25": 727.26, "35": 644.75, "42": 586.99, "50": 520.98},
    "2555": {"nombre": "Herbalife #1 Plátano", "publico": 934.00, "25": 727.26, "35": 644.75, "42": 586.99, "50": 520.98},
    "2057": {"nombre": "Herbalife #1 Vainilla", "publico": 934.00, "25": 727.26, "35": 644.75, "42": 586.99, "50": 520.98},
    "2059": {"nombre": "Herbalife #1 Fresa", "publico": 934.00, "25": 727.26, "35": 644.75, "42": 586.99, "50": 520.98},
    "2158": {"nombre": "Herbalife #1 Piña colada", "publico": 934.00, "25": 727.26, "35": 644.75, "42": 586.99, "50": 520.98},
    "2060": {"nombre": "Herbalife #1 Cookies & cream", "publico": 934.00, "25": 727.26, "35": 644.75, "42": 586.99, "50": 520.98},
    "2154": {"nombre": "Herbalife #1 Frutas tropicales", "publico": 934.00, "25": 727.26, "35": 644.75, "42": 586.99, "50": 520.98},
    "2056": {"nombre": "Herbalife #1 Dulce de leche", "publico": 934.00, "25": 727.26, "35": 644.75, "42": 586.99, "50": 520.98},
    
    #BEBIDAS DE ALOE
    "442K": {"nombre": "Porciones individuales Herbal Aloe Concentrado Mandarina (30 porciones)", "publico": 816.00, "25": 670.22, "35": 612.16, "42": 571.52, "50": 525.07}, 
    "384K": {"nombre": "Herbal Aloe Concentrado Original 473 ml", "publico": 666.00, "25": 515.05, "35": 455.06, "42": 413.06, "50": 365.07}, 
    "1065": {"nombre": "Herbal Aloe Concentrado Mango 473 ml", "publico": 672.00, "25": 521.91, "35": 461.92, "42": 419.92, "50": 371.93}, 
    "2631": {"nombre": "Herbal Aloe Concentrado Mandarina 473 ml", "publico": 672.00, "25": 521.91, "35": 461.92, "42": 419.92, "50": 371.93}, 
    "1610": {"nombre": "Herbal Aloe Concentrado Uva 473 ml", "publico": 672.00, "25": 521.91, "35": 461.92, "42": 419.92, "50": 371.93}, 
    "1189": {"nombre": "Herbal Aloe Concentrado Arándano 473 ml", "publico": 672.00, "25": 521.91, "35": 461.92, "42": 419.92, "50": 371.93}, 
    "1188": {"nombre": "Herbal Aloe Concentrado Mango 1.892 L", "publico": 2434.00, "25": 1890.66, "35": 1673.63, "42": 1521.71, "50": 1348.09},

    #BEVERAGE ENHANCERS
    "214M": {"nombre": "Beverage Enhancers Drink Mix Sandía", "publico": 304.00, "25": 268.27, "35": 254.11, "42": 244.19, "50": 232.85}, 
    "203M": {"nombre": "Beverage Enhancers Drink Mix Piña", "publico": 237.00, "25": 200.71, "35": 186.54, "42": 176.62, "50": 165.29}, 
    "177M": {"nombre": "Beverage Enhancers Drink Mix Explosión azul", "publico": 237.00, "25": 200.71, "35": 186.54, "42": 176.62, "50": 165.29},

    # ENERGIZANTES [cite: 35, 37, 40, 46]
    "208K": {"nombre": "Liftoff Granada", "publico": 1362.00, "25": 1065.85, "35": 947.64, "42": 864.90, "50": 770.33},
    "205K": {"nombre": "Liftoff Naranja", "publico": 1362.00, "25": 1065.85, "35": 947.64, "42": 864.90, "50": 770.33},
    "207K": {"nombre": "Liftoff Frutas tropicales", "publico": 1362.00, "25": 1065.85, "35": 947.64, "42": 864.90, "50": 770.33},
    "132K": {"nombre": "Liftoff Moras", "publico": 1362.00, "25": 1065.85, "35": 947.64, "42": 864.90, "50": 770.33},

    #CAFÉ Y TÉS

    "1428": {"nombre": "Té Verde Granada 48 g", "publico": 801.00, "25": 620.01, "35": 547.79, "42": 497.24, "50": 439.47}, 
    "0922": {"nombre": "Thermojetics Concentrado de Hierbas Limón 51 g", "publico": 516.00, "25": 398.99, "35": 352.52, "42": 319.99, "50": 282.81}, 
    "1638": {"nombre": "Thermojetics Concentrado de Hierbas Chai 51 g", "publico": 516.00, "25": 398.99, "35": 352.52, "42": 319.99, "50": 282.81}, 
    "0963": {"nombre": "Thermojetics Concentrado de Hierbas Original 51 g", "publico": 516.00, "25": 398.99, "35": 352.52, "42": 319.99, "50": 282.81}, 
    "0964": {"nombre": "Thermojetics Concentrado de Hierbas Original 102 g", "publico": 942.00, "25": 729.41, "35": 644.45, "42": 584.97, "50": 517.01}, 
    "483K": {"nombre": "Porciones individuales Thermojetics Concentrado de Hierbas Original", "publico": 286.00, "25": 226.72, "35": 203.04, "42": 186.46, "50": 167.52}, 
    "0085": {"nombre": "N-R-G Té Original 60 g", "publico": 383.00, "25": 296.00, "35": 261.52, "42": 237.38, "50": 209.80}, 
    "2131": {"nombre": "N-R-G Té Manzana verde 60 g", "publico": 383.00, "25": 296.00, "35": 261.52, "42": 237.38, "50": 209.80}, 
    "491K": {"nombre": "Porciones individuales N-R-G Té Original", "publico": 129.00, "25": 106.03, "35": 96.85, "42": 90.42, "50": 83.08}, 
    "494K": {"nombre": "Café Instántaneo 200 g", "publico": 301.00, "25": 255.57, "35": 237.53, "42": 224.90, "50": 210.47}, 
    
    #INFUSIÓN
    "044K": {"nombre": "Infusión Herbal Menta 48 g", "publico": 995.00, "25": 774.16, "35": 685.97, "42": 624.24, "50": 553.69}, 

    #PROTEÍNA EN POLVO
    "0242": {"nombre": "Personalized Protein Powder Original", "publico": 619.00, "25": 478.91, "35": 423.12, "42": 384.08, "50": 339.45}, 
    "2648": {"nombre": "Personalized Protein Powder Frutos rojos", "publico": 636.00, "25": 495.61, "35": 439.83, "42": 400.78, "50": 356.15}, 
    "2146": {"nombre": "Gold Vainilla", "publico": 1273.00, "25": 986.99, "35": 872.91, "42": 793.04, "50": 701.77}, 
    "2147": {"nombre": "Gold Chocolate", "publico": 1366.00, "25": 1057.84, "35": 934.62, "42": 848.37, "50": 749.79}, 
    "289K": {"nombre": "Gold Cacahuate", "publico": 1273.00, "25": 986.99, "35": 872.91, "42": 793.04, "50": 701.77}, 
    "3119": {"nombre": "Protein Mix Ponche de frutas", "publico": 728.00, "25": 582.35, "35": 524.26, "42": 483.59, "50": 437.12}, 
    "3121": {"nombre": "Protein Mix Durazno-mango", "publico": 728.00, "25": 582.35, "35": 524.26, "42": 483.59, "50": 437.12},

    #CONSISTENCIA Y CREMOSIDAD PARA TU BATIDO
    "2644": {"nombre": "Xtra-Shake Nuez", "publico": 992.00, "25": 781.12, "35": 697.13, "42": 638.34, "50": 571.15}, 
    "2641": {"nombre": "Xtra-Shake Original", "publico": 992.00, "25": 781.12, "35": 697.13, "42": 638.34, "50": 571.15}, 
    
    #OTROS NUTRIENTES
    "1095": {"nombre": "Prolessa® Duo", "publico": 890.00, "25": 710.37, "35": 638.61, "42": 588.37, "50": 530.96}, 
    "0077": {"nombre": "TC Formula", "publico": 1106.00, "25": 856.27, "35": 756.53, "42": 686.71, "50": 606.92}, 
    "344K": {"nombre": "Natural-G", "publico": 761.00, "25": 589.15, "35": 520.52, "42": 472.49, "50": 417.59}, 
    
    #FIBRA
    "1829": {"nombre": "Probiótico Sin sabor", "publico": 765.00, "25": 592.06, "35": 523.10, "42": 474.82, "50": 419.65}, 
    "103K": {"nombre": "Active Fiber Complex Select Piña-coco", "publico": 873.00, "25": 684.46, "35": 609.10, "42": 556.36, "50": 496.07}, 
    "2864": {"nombre": "Active Fiber Complex Manzana", "publico": 776.00, "25": 603.49, "35": 534.66, "42": 486.47, "50": 431.40}, 
    "0103": {"nombre": "Thermo-Bond®", "publico": 495.00, "25": 383.08, "35": 338.46, "42": 307.22, "50": 271.53}, 
    
    #PARA ÉL Y ELLA
    "3146": {"nombre": "Niteworks® Naranja-mango", "publico": 1794.00, "25": 1391.74, "35": 1231.13, "42": 1118.71, "50": 990.22}, 
    "3150": {"nombre": "Niteworks® Limón", "publico": 1794.00, "25": 1391.74, "35": 1231.13, "42": 1118.71, "50": 990.22}, 
    "0267": {"nombre": "Betaglucanos Vainilla", "publico": 1399.00, "25": 1083.46, "35": 957.26, "42": 868.92, "50": 767.95}, 
    "0065": {"nombre": "Herbalifeline®", "publico": 920.00, "25": 712.04, "35": 629.10, "42": 571.04, "50": 504.69}, 
    "0032": {"nombre": "Garlic Plus", "publico": 476.00, "25": 368.64, "35": 325.70, "42": 295.64, "50": 261.29}, 
    "0039": {"nombre": "Prelox® Azul", "publico": 1730.00, "25": 1339.10, "35": 1183.12, "42": 1073.93, "50": 949.15},

    #NUTRIENTES PARA TI
    "2374": {"nombre": "Herbalife® Pro Miel-limón y jengibre", "publico": 1040.00, "25": 811.09, "35": 719.62, "42": 655.58, "50": 582.40}, 
    "1094": {"nombre": "Schizandra Plus", "publico": 476.00, "25": 368.64, "35": 325.70, "42": 295.64, "50": 261.29}, 
    
    #NUTRICIÓN PARA LA MUJER
    "1061": {"nombre": "Woman's Choice", "publico": 1037.00, "25": 802.78, "35": 709.27, "42": 643.81, "50": 569.01}, 
    "343K": {"nombre": "Fito Complex", "publico": 502.00, "25": 388.54, "35": 343.29, "42": 311.61, "50": 275.40}, 
    "0565": {"nombre": "Xtra-Cal® Advanced", "publico": 358.00, "25": 276.51, "35": 244.30, "42": 221.75, "50": 195.99}, 
    "0831": {"nombre": "Colágeno Limonada de fresa", "publico": 1330.00, "25": 1032.60, "35": 913.78, "42": 830.61, "50": 735.56}, 
    "323K": {"nombre": "Porciones individuales de Colágeno Limonada de fresa", "publico": 731.00, "25": 582.15, "35": 522.74, "42": 481.16, "50": 433.63}, 
    
    #SNACKS CON PROTEÍNA
    "0364": {"nombre": "Barra Deluxe con Proteína Vainilla con almendra", "publico": 667.00, "25": 571.86, "35": 533.84, "42": 507.23, "50": 476.81}, 
    "0366": {"nombre": "Barra Deluxe con Proteína Limón", "publico": 667.00, "25": 571.86, "35": 533.84, "42": 507.23, "50": 476.81}, 
    "3525": {"nombre": "Barras con Proteína Chocolate", "publico": 538.00, "25": 459.62, "35": 428.47, "42": 406.66, "50": 381.73}, 
    "385K": {"nombre": "Protein Crunch Chocolate", "publico": 480.00, "25": 385.17, "35": 347.54, "42": 321.20, "50": 291.09}, 
    "396K": {"nombre": "Protein Chips Barbecue", "publico": 547.00, "25": 447.26, "35": 407.52, "42": 379.71, "50": 347.92},

    #NUTRICIÓN ESPECÍFICA
    "3115": {"nombre": "Herbalife® Número 2 en tabletas", "publico": 724.00, "25": 560.22, "35": 494.97, "42": 449.29, "50": 397.09}, 
    "2364": {"nombre": "Herbalife® Número 2 en polvo", "publico": 820.00, "25": 634.57, "35": 560.66, "42": 508.92, "50": 449.78}, 
    "345K": {"nombre": "Herbalife® Número 3", "publico": 822.00, "25": 636.12, "35": 562.02, "42": 510.16, "50": 450.88}, 
    "0064": {"nombre": "Arándano con Minerales, Vitaminas y Luteína", "publico": 600.00, "25": 464.46, "35": 410.36, "42": 372.49, "50": 329.21}, 
    "101K": {"nombre": "Balance-M", "publico": 903.00, "25": 698.92, "35": 617.51, "42": 560.52, "50": 495.40}, 
    "440K": {"nombre": "Bisglicinato de Magnesio + Azafrán Manzana canela", "publico": 1024.00, "25": 816.36, "35": 733.65, "42": 675.75, "50": 609.59}, 

    #NUTRICIÓN PARA ATLETAS
    "024K": {"nombre": "BCAAS Manzana verde", "publico": 1347.00, "25": 1090.47, "35": 988.02, "42": 916.31, "50": 834.35}, 
    "3492": {"nombre": "Herbalife® Número 1 Sport Vainilla", "publico": 1539.00, "25": 1210.28, "35": 1078.83, "42": 986.81, "50": 881.65}, 
    "3490": {"nombre": "Strength Chocolate", "publico": 2598.00, "25": 2033.70, "35": 1808.02, "42": 1650.04, "50": 1469.49}, 
    "1120": {"nombre": "Enhanced Protein Powder Natural", "publico": 2423.00, "25": 1900.22, "35": 1691.25, "42": 1544.97, "50": 1377.80}, 
    "1473": {"nombre": "CR7 Drive Açaí", "publico": 887.00, "25": 717.77, "35": 650.12, "42": 602.76, "50": 548.64}, 
    "386K": {"nombre": "Creatina Sin sabor", "publico": 405.00, "25": 322.46, "35": 289.61, "42": 266.61, "50": 240.33}, 

    #HERBALIFE SKIN
    "0766": {"nombre": "Limpiador Cítrico para la Piel", "publico": 467.00, "25": 361.41, "35": 319.31, "42": 289.85, "50": 256.17}, 
    "0767": {"nombre": "Tonificador Energizante de Hierbas", "publico": 418.00, "25": 323.47, "35": 285.80, "42": 259.42, "50": 229.28}, 
    "0768": {"nombre": "Sérum Reductor de Líneas de Expresión", "publico": 1135.00, "25": 878.27, "35": 775.97, "42": 704.36, "50": 622.52}, 
    "0770": {"nombre": "Gel Reafirmante para Contorno de Ojos", "publico": 794.00, "25": 614.42, "35": 542.85, "42": 492.75, "50": 435.50}, 
    "0899": {"nombre": "Crema Humectante FPS 30", "publico": 782.00, "25": 605.42, "35": 534.90, "42": 485.53, "50": 429.12}, 
    "0774": {"nombre": "Crema Hidratante de Noche", "publico": 857.00, "25": 663.25, "35": 586.00, "42": 531.92, "50": 470.11}, 
    "0772": {"nombre": "Exfoliante con Arándanos para el Cutis", "publico": 360.00, "25": 278.30, "35": 245.89, "42": 223.20, "50": 197.26}, 
    "0773": {"nombre": "Mascarilla limpiadora de Arcilla con Menta", "publico": 444.00, "25": 343.35, "35": 303.36, "42": 275.36, "50": 243.37}, 

    #HERBAL ALOE
    "0413": {"nombre": "Herbal Aloe gel corporal con aloe", "publico": 313.00, "25": 242.17, "35": 213.96, "42": 194.22, "50": 171.65},
}
