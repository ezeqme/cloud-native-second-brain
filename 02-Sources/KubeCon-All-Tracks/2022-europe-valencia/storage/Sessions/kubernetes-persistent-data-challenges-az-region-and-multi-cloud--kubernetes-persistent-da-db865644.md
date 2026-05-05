---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Storage"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Chris Milsted", "Ondat", "Patrick McFadin", "DataStax"]
sched_url: https://kccnceu2022.sched.com/event/ytpH/kubernetes-persistent-data-challenges-az-region-and-multi-cloud-patterns-chris-milsted-ondat-patrick-mcfadin-datastax
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Persistent+Data+Challenges+%E2%80%93+AZ%2C+Region+and+Multi-Cloud+Patterns+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kubernetes Persistent Data Challenges – AZ, Region and Multi-Cloud Patterns - Chris Milsted, Ondat & Patrick McFadin, DataStax

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Chris Milsted, Ondat, Patrick McFadin, DataStax
- Schedule: https://kccnceu2022.sched.com/event/ytpH/kubernetes-persistent-data-challenges-az-region-and-multi-cloud-patterns-chris-milsted-ondat-patrick-mcfadin-datastax
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Persistent+Data+Challenges+%E2%80%93+AZ%2C+Region+and+Multi-Cloud+Patterns+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kubernetes Persistent Data Challenges – AZ, Region and Multi-Cloud Patterns.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytpH/kubernetes-persistent-data-challenges-az-region-and-multi-cloud-patterns-chris-milsted-ondat-patrick-mcfadin-datastax
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Persistent+Data+Challenges+%E2%80%93+AZ%2C+Region+and+Multi-Cloud+Patterns+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=N7BYKhpqGXw
- YouTube title: Kubernetes Persistent Data Challenges – AZ, Region and Multi-Clou... Chris Milsted & Patrick McFadin
- Match score: 0.921
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubernetes-persistent-data-challenges-az-region-and-multi-cloud-patter/N7BYKhpqGXw.txt
- Transcript chars: 33397
- Keywords: cluster, cassandra, running, storage, actually, control, clusters, center, operator, multi-cloud, availability, multiple, important, prometheus, essentially, trying, saying, clouds

### Resumo baseado na transcript

good afternoon welcome to our virtual talk uh this is a talk on kubernetes persistent data challenges availability zones regions and multi-cloud patterns so what's the next slide um quick hellos from us uh my name is chris milstead i'm a solution architect at on that so working with customers around all things data and kubernetes and my co-presenter is dr mcfadden um i work in data stacks i work in developer relations and developer experience and i work in the apache cassandra project and a few others but mostly

### Excerpt da transcript

good afternoon welcome to our virtual talk uh this is a talk on kubernetes persistent data challenges availability zones regions and multi-cloud patterns so what's the next slide um quick hellos from us uh my name is chris milstead i'm a solution architect at on that so working with customers around all things data and kubernetes and my co-presenter is dr mcfadden um i work in data stacks i work in developer relations and developer experience and i work in the apache cassandra project and a few others but mostly around open source data and kubernetes i'm also writing a book right now um cloud native data on managing cloud native data on kubernetes available at a bookstore soon chris very soon oh but i've got an order don't you worry yeah well you can you can still download it we'll show the link at the end brilliant and uh before we get into the bulk of the presentation just a quick couple of thanks um to alex and rags alex is one of the engineers on the kate sandra project and has been invaluable help in setting up a lot of the demos and stuff we're going to show later and rags actually built a lot of the multi-cloud crazy demo that we're going to show right at the very end so with that onto the bulk of the presentation and i believe you can leave this off patrick i will so chris i think everyone's going to ask this question why would we even do this so i'm going to walk you through some of the reasons that you may want to be outside of one data center one rack uh and this is a pretty typical question because it does add complexity um it's very simple let's let's be very clear it's very simple to run something that's running on your laptop and that's the most simple way to do it but of course that's not how we put things into production so when we think about production workloads um in trying to conceptualize failure this is this is why we're using multiple az's multiple multi-anything is things around failures and then there's more relevant reasons for contemporary reasons i would say which i'll get into in a minute but like we'll start with just availability zones so availability zones are built by clouds for this problem is to mitigate certain types of failure so i have a little chart here that is is out there you can it's it's nothing new but it's about you know managing your your failures and the service level agreement the slas that people that clouds give on like an individual vm is you get three nines okay that's not bad but it's not great either
