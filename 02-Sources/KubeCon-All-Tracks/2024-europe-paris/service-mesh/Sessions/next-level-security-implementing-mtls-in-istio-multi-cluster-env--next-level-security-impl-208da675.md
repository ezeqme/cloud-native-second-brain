---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Service Mesh"
themes: ["Security", "Networking", "Kubernetes Core"]
speakers: ["Eduardo Bonilla Rodriguez", "Samuel Veloso", "Solo.io"]
sched_url: https://kccnceu2024.sched.com/event/1YeSP/next-level-security-implementing-mtls-in-istio-multi-cluster-environments-using-spire-eduardo-bonilla-rodriguez-samuel-veloso-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Next-Level+Security%3A+Implementing+MTLS+in+Istio+Multi-Cluster+Environments+Using+SPIRE+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Next-Level Security: Implementing MTLS in Istio Multi-Cluster Environments Using SPIRE - Eduardo Bonilla Rodriguez & Samuel Veloso, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Service Mesh]]
- Temas: [[Security]], [[Networking]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Eduardo Bonilla Rodriguez, Samuel Veloso, Solo.io
- Schedule: https://kccnceu2024.sched.com/event/1YeSP/next-level-security-implementing-mtls-in-istio-multi-cluster-environments-using-spire-eduardo-bonilla-rodriguez-samuel-veloso-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Next-Level+Security%3A+Implementing+MTLS+in+Istio+Multi-Cluster+Environments+Using+SPIRE+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Next-Level Security: Implementing MTLS in Istio Multi-Cluster Environments Using SPIRE.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSP/next-level-security-implementing-mtls-in-istio-multi-cluster-environments-using-spire-eduardo-bonilla-rodriguez-samuel-veloso-soloio
- YouTube search: https://www.youtube.com/results?search_query=Next-Level+Security%3A+Implementing+MTLS+in+Istio+Multi-Cluster+Environments+Using+SPIRE+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=83jOYMnmWWY
- YouTube title: Next-Level Security: Implementing MTLS in Istio Multi-Cluster Environments Using SPIRE
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/next-level-security-implementing-mtls-in-istio-multi-cluster-environme/83jOYMnmWWY.txt
- Transcript chars: 26485
- Keywords: server, cluster, workload, certificate, domain, running, request, application, gateway, communication, establish, deploy, multicluster, network, certificates, clusters, thanks, security

### Resumo baseado na transcript

so thank you thank you everyone for attending I know it's Friday it's a bit late so really appreciate it I hope it's it will be an interesting talk and you learn something new so let's start the talk is about implementing mtls in is multicluster environments using Aspire my name is Samu boso I'm software engineer at solo Theo where I'm building a multicluster service mes based on EO and boy my name is edua I am customer success engineer in soloio working on with open source Technologies IO is another way to play with security and SPV ads now I'm going to let um now I'm going to let a for Loop running here with every 2 seconds will make a request to our East Gateway and also if we check the logs

### Excerpt da transcript

so thank you thank you everyone for attending I know it's Friday it's a bit late so really appreciate it I hope it's it will be an interesting talk and you learn something new so let's start the talk is about implementing mtls in is multicluster environments using Aspire my name is Samu boso I'm software engineer at solo Theo where I'm building a multicluster service mes based on EO and boy my name is edua I am customer success engineer in soloio working on with open source Technologies IO enoy Spire so hope you like the talk okay let's start from the beginning so what is mtls most of you probably already know it but for those that don't know it let's start so most of you probably are familiar with TLS it's a traditional protocol used by many websites to encrypt the traffic so in TLS the client has to validate the server from the certificate in order to establish an encrypted communication with mtls both the client and the server authenticate each other so in this case also the server has to uh validate and authenticate the client certificate in order to establish an INR communication this is more powerful because with mtls you can Define policies and restrict the access to your server only to some specific clients so in order to establish or uh yeah to use mtls you need to generate a client certificate and a a certificate and a key for your client and for your server for both of them so this is simple if you only have two apps a client and a server but in Enterprise environments that you are probably more familiar with with kubernetes environments they are really dynamic they the pods are being recreated uh very often so in order to handle the certificates it's you have to use some some kind of tool because it's impossible to handle this mess just with uh with manual actions so the technology that we are going to s that solves this this problem is spify and Spire okay so let's review first what spify and later we will review espire so spify stands for secure production identity framework for everyone it's a an open source standard for securely identifying Software System in Dynamic environments so basically a spif is just uh an standard okay it will it talks about how to design your uh your system to be compliant with the spify so there are several Concepts involved in sp sp architecture that I'm going to to go through the first one is the workload API the workload API is in charge of generating a a document called sbid I'm going to talk about a lot about
