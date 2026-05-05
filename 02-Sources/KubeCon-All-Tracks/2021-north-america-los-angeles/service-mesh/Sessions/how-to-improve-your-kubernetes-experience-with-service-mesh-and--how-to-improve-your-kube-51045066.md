---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Service Mesh"
themes: ["AI ML", "Networking", "Kubernetes Core"]
speakers: ["Maksim Chudnovskii", "Igor Gustomyasov", "Sber"]
sched_url: https://kccncna2021.sched.com/event/lUzy/how-to-improve-your-kubernetes-experience-with-service-mesh-and-mlops-maksim-chudnovskii-igor-gustomyasov-sber
youtube_search_url: https://www.youtube.com/results?search_query=How+to+Improve+Your+Kubernetes+Experience+with+Service+Mesh+and+MLOps+CNCF+KubeCon+2021
slides: []
status: parsed
---

# How to Improve Your Kubernetes Experience with Service Mesh and MLOps - Maksim Chudnovskii & Igor Gustomyasov, Sber

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Maksim Chudnovskii, Igor Gustomyasov, Sber
- Schedule: https://kccncna2021.sched.com/event/lUzy/how-to-improve-your-kubernetes-experience-with-service-mesh-and-mlops-maksim-chudnovskii-igor-gustomyasov-sber
- Busca YouTube: https://www.youtube.com/results?search_query=How+to+Improve+Your+Kubernetes+Experience+with+Service+Mesh+and+MLOps+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre How to Improve Your Kubernetes Experience with Service Mesh and MLOps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lUzy/how-to-improve-your-kubernetes-experience-with-service-mesh-and-mlops-maksim-chudnovskii-igor-gustomyasov-sber
- YouTube search: https://www.youtube.com/results?search_query=How+to+Improve+Your+Kubernetes+Experience+with+Service+Mesh+and+MLOps+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TfDgsEHA1Yo
- YouTube title: How to Improve Your Kubernetes Experience with Service Mesh... Maksim Chudnovskii & Igor Gustomyasov
- Match score: 0.873
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/how-to-improve-your-kubernetes-experience-with-service-mesh-and-mlops/TfDgsEHA1Yo.txt
- Transcript chars: 17678
- Keywords: models, application, metrics, anomaly, mesh, applications, second, average, information, cluster, metric, method, machine, learning, workloads, collect, network, clusters

### Resumo baseado na transcript

hello everybody uh today i would like uh to share our experience uh how to use machine learning algorithm in practice of integration in kubernetes and which algorithms we applied in our experience first of all of all i'd like to introduce ourselves my name is eager gustav messel and i am head of integration department in spairbank technology and i also like to introduce my colleague maxim chugnowski who is a chief software development manager and who will provide some technical insight for you about main topic of presentation

### Excerpt da transcript

hello everybody uh today i would like uh to share our experience uh how to use machine learning algorithm in practice of integration in kubernetes and which algorithms we applied in our experience first of all of all i'd like to introduce ourselves my name is eager gustav messel and i am head of integration department in spairbank technology and i also like to introduce my colleague maxim chugnowski who is a chief software development manager and who will provide some technical insight for you about main topic of presentation today so let's start so in the beginning i'd like to say several words about our organization our big financial and ecosystem organization and main our focus is our best client experience and technological leadership our company takes uh first places in financial services we have a lot of retail clients and corporate clients we have significant market share in russia and also last year's we did a great step in direction of development uh non-finance international services and um development of our ecosystem in the same time uh last year's we introduced a new iet platform with focus of reliability zero downtime and applying machine learning algorithms in all across all services of our platform while we did it and do it you know because we did a lot of work uh in uh in the direction of migration uh our legacy system uh to uh cloud ecosystem and consequently it provides in [Music] it provides a lot of a huge amount of application telemetry which should be collected and transfer processing in appropriate way so of course we have some monitoring issues because our i.t systems landscape is rather large and complex and we have common problems like alerts and metrics hell unclear topology and clear integration [Music] unclean integration uh interactions uh dependencies uh which we understand in real time and also we have some issues connected to elasticity about inefficient inefficient manipulation and efficient rising uh of enough uh resources for our workloads after scaling issues applications start time initials and so on and of course for us uh the main focus is in uh is on a real time interaction so over all latency through complex topology also is the problem for us so if we look at it as a high-level concept i can say that we work with two types of telemetry the basic one which built from the kubernetes tires uh and in this level uh we are most interested in performance of containers alerts which we can collect from containers and then
