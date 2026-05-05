---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Tobias Giese", "Tjark Rasche", "Mercedes-Benz Tech Innovation"]
sched_url: https://kccnceu2024.sched.com/event/1YePd/securing-900-kubernetes-clusters-without-psp-mercedes-benz-journey-to-validatingadmissionpolicies-tobias-giese-tjark-rasche-mercedes-benz-tech-innovation
youtube_search_url: https://www.youtube.com/results?search_query=Securing+900+Kubernetes+Clusters+Without+PSP+-+Mercedes-Benz%27+Journey+to+ValidatingAdmissionPolicies+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Securing 900 Kubernetes Clusters Without PSP - Mercedes-Benz' Journey to ValidatingAdmissionPolicies - Tobias Giese & Tjark Rasche, Mercedes-Benz Tech Innovation

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Tobias Giese, Tjark Rasche, Mercedes-Benz Tech Innovation
- Schedule: https://kccnceu2024.sched.com/event/1YePd/securing-900-kubernetes-clusters-without-psp-mercedes-benz-journey-to-validatingadmissionpolicies-tobias-giese-tjark-rasche-mercedes-benz-tech-innovation
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+900+Kubernetes+Clusters+Without+PSP+-+Mercedes-Benz%27+Journey+to+ValidatingAdmissionPolicies+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Securing 900 Kubernetes Clusters Without PSP - Mercedes-Benz' Journey to ValidatingAdmissionPolicies.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePd/securing-900-kubernetes-clusters-without-psp-mercedes-benz-journey-to-validatingadmissionpolicies-tobias-giese-tjark-rasche-mercedes-benz-tech-innovation
- YouTube search: https://www.youtube.com/results?search_query=Securing+900+Kubernetes+Clusters+Without+PSP+-+Mercedes-Benz%27+Journey+to+ValidatingAdmissionPolicies+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lSGtiVJDXN0
- YouTube title: Securing 900 Kubernetes Clusters Without PSP - Mercedes-Benz' Journey to ValidatingAdmissionPolicies
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/securing-900-kubernetes-clusters-without-psp-mercedes-benz-journey-to/lSGtiVJDXN0.txt
- Transcript chars: 35401
- Keywords: policies, policy, security, validating, custom, emission, admission, cluster, actually, thanks, resources, basically, server, possible, important, pretty, resource, clusters

### Resumo baseado na transcript

thanks for joining our talk how Mercedes-Benz is securing 900 kubernetes clusters uh without part security policies my name is toas giz I'm a software engineer working for Mercedes-Benz Tech Innovation since 2017 I'm a certified kubernetes security specialist and I'm involved into kubernetes since I think 1.7 or something um I'm a former maintainer of the cluster API provider for open stack and I really love hearing and collecting records and I also love optimize my home office desk setup yeah my name is t rash I'm also working

### Excerpt da transcript

thanks for joining our talk how Mercedes-Benz is securing 900 kubernetes clusters uh without part security policies my name is toas giz I'm a software engineer working for Mercedes-Benz Tech Innovation since 2017 I'm a certified kubernetes security specialist and I'm involved into kubernetes since I think 1.7 or something um I'm a former maintainer of the cluster API provider for open stack and I really love hearing and collecting records and I also love optimize my home office desk setup yeah my name is t rash I'm also working as a software engineer at Mercedes ben Tech Innovation uh I've been working with kubernetes since about version 130 I'm not really sure I'm very active in the local kubernetes commun community for example I'm the initiator of uh the kubernetes Meetup in our beautiful suian hometown of and got a few ERS here and also I love making and teaching music especially playing the drums so uh we work for a company called Mercedes-Benz Tech Innovation uh which is a 100% subsidiary and strategic partner of Pharm mercedesbenz uh our company has been developing software phaces Ben since 25 years yeah uh we have around 400 employees who work in different business streams they're called One customer car car sales car after sales and of course from our point of view view the most important stream Technologies in security where few people provide cyber security services for all of Mercedes-Benz and of course we the platform engineering guys uh provide cloud services and infrastructure for all of mercedesbenz uh so our team runs the main managed coronatus platform for all of Mercedes-Benz we run round about thousand kubernetes cluster uh we cannot say the exact number at the moment because it's a full Sal service platform so uh every uh engineering team at Mercedes-Benz could provision or deprovision a cluster at any time but it's around thousand uh they run in eight different zones so uh data centers which are located in two geographic regions one in Germany one in the US and uh they run on premises and in the public Cloud we provide both so uh before we can go into the deep details and how we work in our security setup uh we have first have to explain what managed kues actually means at Mercedes-Benz um so our engineering teams don't have to think about kubernetes operations at all that means they don't have any access to the nodes so no sshing into the nodes but also they don't have to think about stuff like what operating system is the note runnin
