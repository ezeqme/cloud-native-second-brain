---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Unclassified"
themes: ["AI ML", "GitOps Delivery", "Kubernetes Core", "Community Governance"]
speakers: ["Jonathan West", "Red Hat", "Kshama Jain", "Independent Contributor"]
sched_url: https://kccncna2021.sched.com/event/lUzj/manage-more-clusters-with-less-hassle-with-argo-cd-application-sets-jonathan-west-red-hat-kshama-jain-independent-contributor
youtube_search_url: https://www.youtube.com/results?search_query=Manage+More+Clusters+with+Less+Hassle%2C+with+Argo+CD+Application+Sets+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Manage More Clusters with Less Hassle, with Argo CD Application Sets - Jonathan West, Red Hat & Kshama Jain, Independent Contributor

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Jonathan West, Red Hat, Kshama Jain, Independent Contributor
- Schedule: https://kccncna2021.sched.com/event/lUzj/manage-more-clusters-with-less-hassle-with-argo-cd-application-sets-jonathan-west-red-hat-kshama-jain-independent-contributor
- Busca YouTube: https://www.youtube.com/results?search_query=Manage+More+Clusters+with+Less+Hassle%2C+with+Argo+CD+Application+Sets+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Manage More Clusters with Less Hassle, with Argo CD Application Sets.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lUzj/manage-more-clusters-with-less-hassle-with-argo-cd-application-sets-jonathan-west-red-hat-kshama-jain-independent-contributor
- YouTube search: https://www.youtube.com/results?search_query=Manage+More+Clusters+with+Less+Hassle%2C+with+Argo+CD+Application+Sets+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GcvHKc2IHi8
- YouTube title: Manage More Clusters with Less Hassle, with Argo CD Application Sets - Jonathan West & Kshama Jain
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/manage-more-clusters-with-less-hassle-with-argo-cd-application-sets/GcvHKc2IHi8.txt
- Transcript chars: 29847
- Keywords: application, argo, applications, cluster, generator, deploy, template, clusters, resource, repository, within, automatically, generators, controller, custom, single, parameters, resources

### Resumo baseado na transcript

um good morning everyone uh Welcome to our presentation on manage more clusters with les Hassel with Argo CD application set um just to in start by introducing ourselves um my name is Jonathan West I am a senior software engineer at Red Hat coming to you from Toronto Ontario Canada hi hello everyone my name is shama Jan I'm a software engineer and a maintainer of Aro projects and we start we thought we'd start out by giving you a brief elevator pitch say 90 seconds or so on

### Excerpt da transcript

um good morning everyone uh Welcome to our presentation on manage more clusters with les Hassel with Argo CD application set um just to in start by introducing ourselves um my name is Jonathan West I am a senior software engineer at Red Hat coming to you from Toronto Ontario Canada hi hello everyone my name is shama Jan I'm a software engineer and a maintainer of Aro projects and we start we thought we'd start out by giving you a brief elevator pitch say 90 seconds or so on what application sets are how they work and some of the features that you might find interesting there so application sets are a new kubernetes custom resource and a controller that's responsible for managing that custom resource which works alongside an existing argocd install so you specify uh with your application set a template a generator which is used to cust cize that template and then the application set goes and creates applications based on the template and Generator combination that you specified so you can think of application sets as being kind of like a factory for AG CD application you specify the template the generator and then the application set controller automatically outputs a bunch of applications that meet your specific application specifications and that lets you do some really neat things like say uh if you've got uh git repositories containing 50 applications that you want to deploy Loy and you want to deploy them to 50 clusters you can manage all of those combinations all those deployment combinations using uh argocd applications within an Argo CD application set as a single unit so it's very easy to manage um those cluster deployments can be customized using data from external data sources um so for example as you scale up to add new clusters um as you add new git repositories as you new add new applications to your existing git repositories those will automatically be detected by application sets and deployed to your cluster using the template um it does automatically re react to new external changes on the fly so as I said uh infrastructure changes uh correspond to Cluster changes and that's both quick and customizable finally application sets are based on Aro CD applications um so for folks that are already familiar with Argo CD uh and know and love it you're going to get all the power that comes with Argo CD with Argo CD application sets So speaking of harnessing the power of ARG CD I will now hand it over to sha to talk about argro CD and kops thank you
