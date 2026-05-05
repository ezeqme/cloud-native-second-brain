---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Application + Delivery"
themes: ["Storage Data", "GitOps Delivery"]
speakers: ["Mohit Suman", "Zbynek Roubalik", "Red Hat"]
sched_url: https://kccnceu2023.sched.com/event/1HybE/processing-of-amsterdam-city-data-with-vendor-agnostic-serverless-functions-mohit-suman-zbynek-roubalik-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Processing+of+Amsterdam+City+Data+with+Vendor+Agnostic+Serverless+Functions+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Processing of Amsterdam City Data with Vendor Agnostic Serverless Functions - Mohit Suman & Zbynek Roubalik, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Application + Delivery]]
- Temas: [[Storage Data]], [[GitOps Delivery]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mohit Suman, Zbynek Roubalik, Red Hat
- Schedule: https://kccnceu2023.sched.com/event/1HybE/processing-of-amsterdam-city-data-with-vendor-agnostic-serverless-functions-mohit-suman-zbynek-roubalik-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Processing+of+Amsterdam+City+Data+with+Vendor+Agnostic+Serverless+Functions+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Processing of Amsterdam City Data with Vendor Agnostic Serverless Functions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HybE/processing-of-amsterdam-city-data-with-vendor-agnostic-serverless-functions-mohit-suman-zbynek-roubalik-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Processing+of+Amsterdam+City+Data+with+Vendor+Agnostic+Serverless+Functions+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UvxYQd_IGXQ
- YouTube title: Processing of Amsterdam City Data with Vendor Agnostic Serverless Functions - M Suman & Z Roubalik
- Match score: 0.968
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/processing-of-amsterdam-city-data-with-vendor-agnostic-serverless-func/UvxYQd_IGXQ.txt
- Transcript chars: 31076
- Keywords: function, application, serverless, functions, deploy, already, basically, cluster, weather, native, deployed, broker, actually, events, multiple, running, responder, specific

### Resumo baseado na transcript

hello everybody Welcome to our session about uh vendor agnostic service functions we will be presenting today with Mohit so first let's introduce ourselves my name is robotic I'm based in Czech Republic I'm in general working at redhat in openshift serverless team I'm a member of creative community so I'm a member of community POC I'm also maintainer of projected so if you have any questions on those two projects feel free to ask me good afternoon everyone my name is Mohit subin and I work at red hat

### Excerpt da transcript

hello everybody Welcome to our session about uh vendor agnostic service functions we will be presenting today with Mohit so first let's introduce ourselves my name is robotic I'm based in Czech Republic I'm in general working at redhat in openshift serverless team I'm a member of creative community so I'm a member of community POC I'm also maintainer of projected so if you have any questions on those two projects feel free to ask me good afternoon everyone my name is Mohit subin and I work at red hat and I'm a senior product manager working around Red Hat developer tools I'm based out of India and today we are going through some of the cool stuffs what we do around serverless K native and functions cool so this is the shoulder agenda so we will do some introduction this will be done right and then we are talking about serverless functions so maybe we'll say what the servers actually is then then we will show show the demo okay so what is serverless I I bet the majority of people when they serve serverless they think okay that's AWS Lambda right but there might be different different ways how to achieve those similar capabilities uh so for example this is a definition from cncf I won't read the whole definition but basically the the main point is that uh serverless there are applications that do not require server management and they have like a very simple deployment model and they should be executed and scaled uh based on the demand in the in the in the very specific moment so if I can summarize this in a few bullet points so serverless it's like Auto scaling right this is important feature of serverless so scale to zero simplified development and deployment model and by its nature the service server services or functions are even driven so they should be asynchronous so we need to take this into consideration when we are let's say building our our solution based on the serverless approaches also the serverless I don't want to deal with the server configuration or or with the infrastructure configuration this should be very very simple with a very nice ux also when we are talking about serverless there's like serverless functions function as a service there are different opinions on this on this on these terms so this is how we see it actually so for us the serverless is a deployment model that basically abstracts the the way the the way that we deploy the application on the on the infrastructure so I've started the infrastructure it provides the capabili
