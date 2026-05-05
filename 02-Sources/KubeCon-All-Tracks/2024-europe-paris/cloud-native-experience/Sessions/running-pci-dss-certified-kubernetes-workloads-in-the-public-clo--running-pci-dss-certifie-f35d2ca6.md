---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Cloud Native Experience"
themes: ["Kubernetes Core"]
speakers: ["Stephen Hoekstra", "Marcel Bezemer", "Schuberg Philis"]
sched_url: https://kccnceu2024.sched.com/event/1YeQJ/running-pci-dss-certified-kubernetes-workloads-in-the-public-cloud-stephen-hoekstra-marcel-bezemer-schuberg-philis
youtube_search_url: https://www.youtube.com/results?search_query=Running+PCI-DSS+Certified+Kubernetes+Workloads+in+the+Public+Cloud+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Running PCI-DSS Certified Kubernetes Workloads in the Public Cloud - Stephen Hoekstra & Marcel Bezemer, Schuberg Philis

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Stephen Hoekstra, Marcel Bezemer, Schuberg Philis
- Schedule: https://kccnceu2024.sched.com/event/1YeQJ/running-pci-dss-certified-kubernetes-workloads-in-the-public-cloud-stephen-hoekstra-marcel-bezemer-schuberg-philis
- Busca YouTube: https://www.youtube.com/results?search_query=Running+PCI-DSS+Certified+Kubernetes+Workloads+in+the+Public+Cloud+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Running PCI-DSS Certified Kubernetes Workloads in the Public Cloud.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQJ/running-pci-dss-certified-kubernetes-workloads-in-the-public-cloud-stephen-hoekstra-marcel-bezemer-schuberg-philis
- YouTube search: https://www.youtube.com/results?search_query=Running+PCI-DSS+Certified+Kubernetes+Workloads+in+the+Public+Cloud+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OiO7ySxWiQs
- YouTube title: Running PCI-DSS Certified Kubernetes Workloads in the Public Cloud
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/running-pci-dss-certified-kubernetes-workloads-in-the-public-cloud/OiO7ySxWiQs.txt
- Transcript chars: 32260
- Keywords: basically, actually, environment, cluster, container, requirements, policies, network, traffic, running, containers, process, access, policy, production, security, requirement, applications

### Resumo baseado na transcript

Welcome to our talk about running certified uh PCI DSS workloads in the public Cloud uh on cuberes a short agenda about what we'll be covering today we're going to talk a bit about us uh myself and myel while we're here a very short what and why of PCR DSS how we are able to meet PC DSS requirements using cncf and open source projects and then short up uh recap at the end so to start my name is Steven uh and this is Mel we work at

### Excerpt da transcript

Welcome to our talk about running certified uh PCI DSS workloads in the public Cloud uh on cuberes a short agenda about what we'll be covering today we're going to talk a bit about us uh myself and myel while we're here a very short what and why of PCR DSS how we are able to meet PC DSS requirements using cncf and open source projects and then short up uh recap at the end so to start my name is Steven uh and this is Mel we work at Shuba phis as Mission critical engineers and my background is running uh backend services or providing services to customers and myselves background is more in supporting and and enabling the developer teams that we uh support we started this journey around 3 years ago um provisioning our first cluster in Amazon to help a customer migrate from on Prem to to the cloud they are we'll cover them in a bit but basically they are already PCR DSS uh certified and part of the task for us was to uh help them still maintain this W in the cloud we also hoping to use this talk to help demystify some of the aura around PC DSS um when chatting to some colleagues uh at our company outside our team or even outside our company there's like this Aura of specialness or complexity uh about with PCI DSS and hopefully when I show you is not all that bad so a short uh bit about uh sh phis and while Mission critical engineer so we use this term uh to describe the sort of work that we do I guess it's more close to an SRE sort of role um but it really matches the the environments we look after so we tend to look after like Mission critical uh environments so these are the the the bits of it infrastructure that's very critical to a Company Success so if this part is uh not running not functional then it really impacts that uh that customers uh ability to operate and that's that's what we tend to help them with uh um yeah and and M and some others are in a team that is servicing one of these uh critical customers with this with this transition from un Prem to the cloud and we going to talk a bit about that so this customer is called CCV um they're more known in the Netherlands and in Belgium maybe uh in the B area but they are a transaction processor and they are one of two transaction processors in in Netherlands and Belgium so to be very short if you are making online payment or you uh are tapping your phone or card or one of these machines there's a very high chance that um you are having your payments run through their system so while we can't uh dulge
