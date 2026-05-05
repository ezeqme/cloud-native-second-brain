---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Machine Learning + Data"
themes: ["AI ML", "Platform Engineering", "Storage Data"]
speakers: ["Alejandro Saucedo", "The Institute for Ethical AI", "Machine Learning"]
sched_url: https://kccncna2022.sched.com/event/182EO/metaops-metadata-operations-for-end-to-end-data-machine-learning-platforms-alejandro-saucedo-the-institute-for-ethical-ai-machine-learning
youtube_search_url: https://www.youtube.com/results?search_query=MetaOps%3A+Metadata+Operations+For+End-To-End+Data+%26+Machine+Learning+Platforms+CNCF+KubeCon+2022
slides: []
status: parsed
---

# MetaOps: Metadata Operations For End-To-End Data & Machine Learning Platforms - Alejandro Saucedo, The Institute for Ethical AI & Machine Learning

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Storage Data]]
- País/cidade: United States / Detroit
- Speakers: Alejandro Saucedo, The Institute for Ethical AI, Machine Learning
- Schedule: https://kccncna2022.sched.com/event/182EO/metaops-metadata-operations-for-end-to-end-data-machine-learning-platforms-alejandro-saucedo-the-institute-for-ethical-ai-machine-learning
- Busca YouTube: https://www.youtube.com/results?search_query=MetaOps%3A+Metadata+Operations+For+End-To-End+Data+%26+Machine+Learning+Platforms+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre MetaOps: Metadata Operations For End-To-End Data & Machine Learning Platforms.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182EO/metaops-metadata-operations-for-end-to-end-data-machine-learning-platforms-alejandro-saucedo-the-institute-for-ethical-ai-machine-learning
- YouTube search: https://www.youtube.com/results?search_query=MetaOps%3A+Metadata+Operations+For+End-To-End+Data+%26+Machine+Learning+Platforms+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wzbj7LcQ2Ek
- YouTube title: MetaOps: Metadata Operations For End-To-End Data & Machine Learning Platforms - Alejandro Saucedo
- Match score: 0.972
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/metaops-metadata-operations-for-end-to-end-data-machine-learning-platf/wzbj7LcQ2Ek.txt
- Transcript chars: 37382
- Keywords: machine, learning, metadata, actually, systems, models, question, inference, questions, challenges, around, standards, artifact, deployed, protocol, production, standardized, management

### Resumo baseado na transcript

all right welcome everybody uh to the yeah uh talk today which we're going to be delving into uh yeah really uh interesting uh topic that is going to have a lot of call to actions for the community um that you know we'll have to get together collaborate in order to make this a success so today's talk is metadata operations for end-to-end data and machine learning platforms the objective of this talk is to give an intuition primarily on the challenges uh that are being faced when it adopted approach into what is the shape of the model inputs and the shape of the pipeline inputs and outputs so once you have this this understanding and you know what the shapes of your machine learning systems are you can start thinking of the of the data Centric view of your machine Learning Systems in in in in the perspective of what what is the value that I'm that I'm that I'm receiving from these services that I have deployed and more importantly how do I then map this

### Excerpt da transcript

all right welcome everybody uh to the yeah uh talk today which we're going to be delving into uh yeah really uh interesting uh topic that is going to have a lot of call to actions for the community um that you know we'll have to get together collaborate in order to make this a success so today's talk is metadata operations for end-to-end data and machine learning platforms the objective of this talk is to give an intuition primarily on the challenges uh that are being faced when it comes to managing machine learning systems at scale and specifically how the metadata within the systems differs uh in in regards to when it's com compared to the more traditional Data Systems so let's dive straight into it a little bit about myself my name is Alejandro I'm engineering director at Selden Technologies uh we're a company that focuses on deployments and monitoring of machine learning models at scale and we're the authors of one of the most popular machine learning deployment Frameworks in kubernetes called seldom core I'm also a chief scientist at The Institute for ethical AI research centered based in the UK that focuses on developing Frameworks for the responsible design operation of machine learning systems and I'm also a governing council member at large at the ACM so today what are we going to be covering we're going to be giving some intuition on the motivations why should we care and challenges of how is it how is it different to traditional metadata we're going to talk about some of those differences being the relationships that we're dealing with the entities in the mlops world we're going to talk about some ways in which we're looking to tackle these challenges through what we can refer to as the open inference protocol as well as the open inference schema finally we're going to have a call to action for basically things that we can do as a community to continue driving this forward so let's dive straight into it so just to set the scene um you know just a picture uh early uh you know 2010s how it all started a handful of Frameworks in the mlops ecosystem in the ml ecosystem that you could pick and choose uh to be able to even productionize your machine learning models how it's going today uh you know there is a uh ever growing number of envelopes tools that are appearing every single day that are tackling pretty much very similar challenges across very uh analogous areas in the mlops life cycle and envelope stack so one of the things that we're seeing an
