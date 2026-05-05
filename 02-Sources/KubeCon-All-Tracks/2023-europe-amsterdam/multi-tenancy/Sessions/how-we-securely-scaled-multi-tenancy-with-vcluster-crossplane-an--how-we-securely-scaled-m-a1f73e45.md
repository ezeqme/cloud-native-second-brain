---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Multi-tenancy"
themes: ["Security", "GitOps Delivery", "Kubernetes Core", "SRE Reliability"]
speakers: ["Ilia Medvedev", "Kostis Kapelonis", "Codefresh"]
sched_url: https://kccnceu2023.sched.com/event/1HyYu/how-we-securely-scaled-multi-tenancy-with-vcluster-crossplane-and-argo-cd-ilia-medvedev-kostis-kapelonis-codefresh
youtube_search_url: https://www.youtube.com/results?search_query=How+We+Securely+Scaled+Multi-Tenancy+with+VCluster%2C+Crossplane%2C+and+Argo+CD+CNCF+KubeCon+2023
slides: []
status: parsed
---

# How We Securely Scaled Multi-Tenancy with VCluster, Crossplane, and Argo CD - Ilia Medvedev & Kostis Kapelonis, Codefresh

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Multi-tenancy]]
- Temas: [[Security]], [[GitOps Delivery]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ilia Medvedev, Kostis Kapelonis, Codefresh
- Schedule: https://kccnceu2023.sched.com/event/1HyYu/how-we-securely-scaled-multi-tenancy-with-vcluster-crossplane-and-argo-cd-ilia-medvedev-kostis-kapelonis-codefresh
- Busca YouTube: https://www.youtube.com/results?search_query=How+We+Securely+Scaled+Multi-Tenancy+with+VCluster%2C+Crossplane%2C+and+Argo+CD+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre How We Securely Scaled Multi-Tenancy with VCluster, Crossplane, and Argo CD.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyYu/how-we-securely-scaled-multi-tenancy-with-vcluster-crossplane-and-argo-cd-ilia-medvedev-kostis-kapelonis-codefresh
- YouTube search: https://www.youtube.com/results?search_query=How+We+Securely+Scaled+Multi-Tenancy+with+VCluster%2C+Crossplane%2C+and+Argo+CD+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hFiHU6W4_z0
- YouTube title: How We Securely Scaled Multi-Tenancy with VCluster, Crossplane... Ilia Medvedev & Kostis Kapelonis
- Match score: 0.856
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/how-we-securely-scaled-multi-tenancy-with-vcluster-crossplane-and-argo/hFiHU6W4_z0.txt
- Transcript chars: 31584
- Keywords: cluster, resources, clusters, deploy, argo, customer, v-cluster, question, virtual, basically, create, provider, namespace, resource, access, customers, instance, inside

### Resumo baseado na transcript

so welcome to this coupon presentation about how you used the cluster cross plane and argosity for multi-tenancy I'm kostis capellanis I'm working as a developer Advocate at codefresh and with me I have Ilia our devops engineer at code fresh and the problem we are going to talk about today is how we provided hosted Argos at the instances to the masses we both work for code fresh it's a software delivery platform it has a CI CD and github's component it's if you want to know more about

### Excerpt da transcript

so welcome to this coupon presentation about how you used the cluster cross plane and argosity for multi-tenancy I'm kostis capellanis I'm working as a developer Advocate at codefresh and with me I have Ilia our devops engineer at code fresh and the problem we are going to talk about today is how we provided hosted Argos at the instances to the masses we both work for code fresh it's a software delivery platform it has a CI CD and github's component it's if you want to know more about codefresh we have a booth outside but today we're going to talk about a very specific problem that we wanted to solve so customers can go to the contrast website they sign up they open an account with us and then after some minutes they get an Argos in the instance for them just for them credit for them it's open to everybody so we don't know how many users we have in advance and usually it should be fully automated we don't want to open a ticket to create a cluster for them we don't want them to send an email we want to to be completely self-serve so that's the problem we wanted to to solve and essentially give an Argo instance to to everybody if you know the name so what are the possible solutions if you are familiar with Argo CD Argo CD on its own has an installation mode where you install it on a namespace so you split in the installation into two parts first you install the CR this only on the parent cluster and then for its name space you install an Argos in the instance that works only on that namespace and after you do that the customers come in and they can connect their own clusters to this to their own argosity instance so essentially it's customer has a namespace on a third cluster now this could work in theory it's very easy for us because we have a single cluster it's a centralized it's also resource efficient we can use all the auto scaling methods that we have for kubernetes creating a namespace is uh super fast so it's very easy for customers to get what they want right away but it's not secure by default so there is no isolation between them spaces we need to set up policies a set of quotas do something for isolation you also have the usual problems with resource servation if somebody is doing something that gets stuck the whole system will have issues and also specifically for us because we're installing Argo CD and we want in its tenant to get Argo CD Argo CD has its own crd so we would have problems because we can only use one crd for everybody one crd in
