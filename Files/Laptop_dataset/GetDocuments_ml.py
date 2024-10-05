import xml.etree.ElementTree as ET
"""https://docs.python.org/2/library/xml.etree.elementtree.html"""

class Review:
    def __init__(self,review_, aspect_, polarity_):
        self.review = review_
        self.aspect = aspect_
        self.polarity = polarity_

class Token:
    def __init__(self, token, posicion, inicio, fin):
        self.token = token
        self.posicion = posicion
        self.inicio = inicio
        self.fin = fin

def Review_target(ventana_i,posicion,ventana_f,Review_tokens):
    review_target = ""
    for token in Review_tokens:
        if token.posicion >= ventana_i and token.posicion <= ventana_f:
            review_target += token.token + ' '
    
    return review_target

def Get_ReviewTarget(review, target, from_, to_ , window):
   # ------------------------------------------------
   # Get tokens from review and identify position, from and to for each one
   Review_tokens = []
   start_ = 0
   end_ = 0
   posicion_ = 0
   for i in range(len(review)):    
      if review[i] == ' ':
         end_ = i
         Review_tokens.append(Token(review[start_:end_],posicion_,start_, end_ - 1))
         start_ = i + 1
         posicion_ += 1
   Review_tokens.append(Token(review[start_:],posicion_,start_, len(review)-1))

   review_target = ""
   for token in Review_tokens:
      if str(token.inicio) == from_:
         posicion_target = token.posicion
         ventana_i = token.posicion - window
         ventana_f = token.posicion + window
         
         if ventana_i < 0:
               ventana_i = 0
         
         if ventana_f > posicion_:
               ventana_f = posicion_

         review_target = Review_target(ventana_i,posicion_target,ventana_f,Review_tokens)

   return review_target


Categories  = []
Polarities = []
Reviews = []
#Open dataset:
# tree = ET.parse('SemEval-2016ABSA Restaurants-Spanish_Train_Subtask1.xml')
tree = ET.parse('laptops-trial.xml')

# Get the root element:
raiz = tree.getroot()
window = 3

for review in raiz:
   print(review.tag)
   print(review.get('id')) #Get usuario

   print(review.find('text').text) #Get review
   review_ = review.find('text').text #review
   Aspects  = []
   Polarities = []
   

   
   for tags in review.iter('aspectTerms'):
      print(tags.tag)

      for e in review.iter('aspectTerm'):             

         #------------------------------------------   
         # Get aspect 
         aspect_ = e.get('term')               
         from_ = e.get('from')
         to_ = e.get('to')
         polarity_ = e.get('polarity')

         
         # if aspect == '' or aspect == "NULL":
         if polarity_ != "conflict":
            ireview = Review(review_,aspect_,polarity_) # REVIEW object
            Reviews.append(ireview)
         # else:
         #    review_target = Get_ReviewTarget(review,aspect,from_, to_, window)
         #    ireview = Review(review_target,category, polarity) # REVIEW object
         #    Reviews.append(ireview)


#File
dataset_Test_spanish_doc = open('S3_EN_LAPTOPS_TEST_ABAA.reviews.gold','w',encoding='utf-8') 
dataset_Test_spanish_aspect = open('S3_EN_LAPTOPS_TEST_ABAA.aspects.gold','w',encoding='utf-8') 
dataset_Test_spanish_polarities = open('S3_EN_LAPTOPS_TEST_ABAA.polarities.gold','w',encoding='utf-8')

for review in Reviews:
   dataset_Test_spanish_doc.write(review.review + "\n")
   dataset_Test_spanish_aspect.write(review.aspect + "\n")
   dataset_Test_spanish_polarities.write(review.polarity + "\n")


dataset_Test_spanish_doc.close()
dataset_Test_spanish_aspect.close()
dataset_Test_spanish_polarities.close()