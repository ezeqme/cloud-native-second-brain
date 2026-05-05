---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Application + Development"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Srinidhi S", "Venkatesan Vaidyanathan", "Razorpay"]
sched_url: https://kccncna2021.sched.com/event/lV20/improving-dev-experience-how-we-built-a-cloud-native-dev-stack-at-scale-srinidhi-s-venkatesan-vaidyanathan-razorpay
youtube_search_url: https://www.youtube.com/results?search_query=Improving+Dev+Experience%3A+How+We+Built+a+Cloud+Native+Dev+Stack+At+Scale+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Improving Dev Experience: How We Built a Cloud Native Dev Stack At Scale - Srinidhi S & Venkatesan Vaidyanathan, Razorpay

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Application + Development]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: United States / Los Angeles
- Speakers: Srinidhi S, Venkatesan Vaidyanathan, Razorpay
- Schedule: https://kccncna2021.sched.com/event/lV20/improving-dev-experience-how-we-built-a-cloud-native-dev-stack-at-scale-srinidhi-s-venkatesan-vaidyanathan-razorpay
- Busca YouTube: https://www.youtube.com/results?search_query=Improving+Dev+Experience%3A+How+We+Built+a+Cloud+Native+Dev+Stack+At+Scale+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Improving Dev Experience: How We Built a Cloud Native Dev Stack At Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV20/improving-dev-experience-how-we-built-a-cloud-native-dev-stack-at-scale-srinidhi-s-venkatesan-vaidyanathan-razorpay
- YouTube search: https://www.youtube.com/results?search_query=Improving+Dev+Experience%3A+How+We+Built+a+Cloud+Native+Dev+Stack+At+Scale+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=f-w5Nh92dt8
- YouTube title: Improving Dev Experience: How We Built a Cloud Native Dev St... Srinidhi S & Venkatesan Vaidyanathan
- Match score: 0.856
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/improving-dev-experience-how-we-built-a-cloud-native-dev-stack-at-scal/f-w5Nh92dt8.txt
- Transcript chars: 28314
- Keywords: developers, resources, infrastructure, request, header, developer, container, development, working, deployment, environment, running, command, application, solution, ephemeral, created, change

### Resumo baseado na transcript

hi my name is venkat and i work at razer bay as a senior architect and i have with me my colleague srinidhi who works as a senior software engineer at recipe today we would love to talk about improving the developer experience and how we build a cloud native dev stack for hundreds of engineers a quick overview into what razer pay does razer pay enables frictionless payment banking and lending experiences for different classes of merchants of various scales and sizes today we process billions of transactions for

### Excerpt da transcript

hi my name is venkat and i work at razer bay as a senior architect and i have with me my colleague srinidhi who works as a senior software engineer at recipe today we would love to talk about improving the developer experience and how we build a cloud native dev stack for hundreds of engineers a quick overview into what razer pay does razer pay enables frictionless payment banking and lending experiences for different classes of merchants of various scales and sizes today we process billions of transactions for millions of merchants across the country razer bay has been at the forefront of innovation over the last several years in terms of transforming the financial ecosystem in the country a big motivation into why we actually embarked upon this journey over the last four years our engineering head crown head count has actually grown up by 10x in that process we have scaled up our teams into full-fledged pods and views four views and 30-plus bots we had embarked upon microservices journey a couple of years back and today we have about 100 plus micro services on it just in the last two years uh the number of micro services has increased to about 50.

uh we've had three company acquisition three acquisitions uh across the course of time that has led to a polyglot uh stack of various languages like php gold and python java etc overall we do roughly about thousand finder deployments per month now a quick look at what our ci cd practice looks like this is not really very different from the way many companies operate but just to give a perspective and sort of build up the motivation for the kind of problems that you're dealing with uh at a very very high level developers commit code into github we heavily use github ci integration github actions for our ci integration uh so the git of actions basically builds uh images which are docker images uh runs a variety of unit tests and pushes it into our private doc registry as soon as these images are available but the developers uh typically start deploying that code with spinnaker spinnaker is a open source uh developer cd platform created by netflix so the deployment process is very similar in a pre-broad environment they they run a variety of integration tests load tests if needed and a bunch of other tests once the developer is satisfied with the test reports the developer goes on to deploy the code in a canary environment uh again via spin occurs kayanta we run a variety of canary threshold metrics and what that
