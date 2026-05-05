---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "SRE Reliability"]
speakers: ["Alejandro Saucedo", "The Institute for Ethical AI", "Machine Learning"]
sched_url: https://kccnceu2021.sched.com/event/iE3X/automated-machine-learning-performance-evaluation-alejandro-saucedo-the-institute-for-ethical-ai-machine-learning
youtube_search_url: https://www.youtube.com/results?search_query=Automated+Machine+Learning+Performance+Evaluation+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Automated Machine Learning Performance Evaluation - Alejandro Saucedo, The Institute for Ethical AI & Machine Learning

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: Virtual / Virtual
- Speakers: Alejandro Saucedo, The Institute for Ethical AI, Machine Learning
- Schedule: https://kccnceu2021.sched.com/event/iE3X/automated-machine-learning-performance-evaluation-alejandro-saucedo-the-institute-for-ethical-ai-machine-learning
- Busca YouTube: https://www.youtube.com/results?search_query=Automated+Machine+Learning+Performance+Evaluation+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Automated Machine Learning Performance Evaluation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE3X/automated-machine-learning-performance-evaluation-alejandro-saucedo-the-institute-for-ethical-ai-machine-learning
- YouTube search: https://www.youtube.com/results?search_query=Automated+Machine+Learning+Performance+Evaluation+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Z53KkGThFNo
- YouTube title: Automated Machine Learning Performance Evaluation - Alejandro Saucedo
- Match score: 0.925
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/automated-machine-learning-performance-evaluation/Z53KkGThFNo.txt
- Transcript chars: 25324
- Keywords: actually, basically, number, workflow, performance, perspective, parameters, benchmarking, machine, actual, argo, learning, evaluation, perform, workers, running, leverage, requests

### Resumo baseado na transcript

hello my name is alejandro saucedo and today we're going to be covering automated machine learning performance benchmarking and evaluation at scale a bit about myself i am engineering director at southern technologies chief scientist at the institute for ethical ai and governing council member at large at the acm we have a lot of topics to cover so let's dive straight into it today we're going to be diving into the motivations for automated benchmarking uh we're going to be covering some techniques and tools that you will be

### Excerpt da transcript

hello my name is alejandro saucedo and today we're going to be covering automated machine learning performance benchmarking and evaluation at scale a bit about myself i am engineering director at southern technologies chief scientist at the institute for ethical ai and governing council member at large at the acm we have a lot of topics to cover so let's dive straight into it today we're going to be diving into the motivations for automated benchmarking uh we're going to be covering some techniques and tools that you will be able to use to perform uh benchmarking against the deployed model we're going to talk about then the the ways in which this can be automated as well as how to automate this with uh workflow management systems and talk about what those are and then finally we're going to be covering a couple of uh examples hands-on examples that will show you how you're able to adopt this in your workflows so let's start with a familiar model right and this would be the hello world of machine learning the c410 classifier what we have here is basically a model that takes uh an image and is able to predict what class this image is and from that perspective in this case this is the image of a truck and is predicting class number nine which would be in this case the image of a truck now from that perspective what we want to do is we want to um see it from the productionization perspective right so of course there's going to be some uh complex experimentation process that would be carried out by uh the respective you know data scientists and the main experts to find what is the best performing type of model in this case we would be able to work with an already trained model which we will be able to fetch with some of the utilities in one of our open source frameworks so from that perspective we already have this tensorflow resnet 32 trained model what we are able to do is we now are able to ask the question well how do we productionize it and we can actually luckily use a lot of the tools available in the case of this talk we're going to be using this tool called selden core seldom core is a framework that allows you to productionize your model artifacts or code into a fully fledged microservice that can be scaled in kubernetes clusters and as you will see uh throughout the rest of the talk uh the the microservices that get produced uh have a rest and grpc api it produces metrics it it has some ability of logs but ultimately this is basically what we will be
