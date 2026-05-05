---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Jie Yu", "Prashanth Venugopal", "Google"]
sched_url: https://kccncna2024.sched.com/event/1i7pE/how-google-built-a-new-cloud-on-top-of-kubernetes-jie-yu-prashanth-venugopal-google
youtube_search_url: https://www.youtube.com/results?search_query=How+Google+Built+a+New+Cloud+on+Top+of+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# How Google Built a New Cloud on Top of Kubernetes - Jie Yu & Prashanth Venugopal, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Jie Yu, Prashanth Venugopal, Google
- Schedule: https://kccncna2024.sched.com/event/1i7pE/how-google-built-a-new-cloud-on-top-of-kubernetes-jie-yu-prashanth-venugopal-google
- Busca YouTube: https://www.youtube.com/results?search_query=How+Google+Built+a+New+Cloud+on+Top+of+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre How Google Built a New Cloud on Top of Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pE/how-google-built-a-new-cloud-on-top-of-kubernetes-jie-yu-prashanth-venugopal-google
- YouTube search: https://www.youtube.com/results?search_query=How+Google+Built+a+New+Cloud+on+Top+of+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6OnZrBY_nFM
- YouTube title: How Google Built a New Cloud on Top of Kubernetes - Jie Yu & Prashanth Venugopal, Google
- Match score: 0.822
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/how-google-built-a-new-cloud-on-top-of-kubernetes/6OnZrBY_nFM.txt
- Transcript chars: 42554
- Keywords: cluster, networking, network, clusters, support, management, actually, virtual, policy, multicluster, multiple, container, customer, customers, containers, google, workloads, policies

### Resumo baseado na transcript

so um so hello everyone so my name is G this is Pam so we're going to be talking about how Google built a new Cloud on top of kubernetes unfortunately s cannot be joining this presentation so going to just be me and pan presenting this all right so um many of you are familiar with the hyperscaler kind of public cloud computing platform and the benefit that the benefit that um they offer and as more and more workloads are shifting to the public Cloud so uh at

### Excerpt da transcript

so um so hello everyone so my name is G this is Pam so we're going to be talking about how Google built a new Cloud on top of kubernetes unfortunately s cannot be joining this presentation so going to just be me and pan presenting this all right so um many of you are familiar with the hyperscaler kind of public cloud computing platform and the benefit that the benefit that um they offer and as more and more workloads are shifting to the public Cloud so uh at Google we notice some customer actually want the the the benefit of the cloud but they want that in a disconnected environment so those en those customers would love to leverage the benefit of cloud computing but due to like a regulatory or security reasons they can cannot just use public offerings so um to to better serve those customers so in 2021 so we start an effort trying to build a new Cloud kind of air Gable Cloud at Google so we want that cloud to be kind of um like air Gable and look and feel just like our Cloud offerings and uh but can be completely disconnected from the internet and uh and and more important is able to kind of scale from a very small scale like a few racks to a large scale so um of course this is like a very audacious kind of undertaking and the the big natural question is um how to do this so uh of course when you're building something new um the first thing you do is actually look around and see uh what have been built already and whether you can reuse those things right so uh over the years Google has built like a a kind of like very amazing internal technology like B stubby classes spanner and more and this internal technology enable us to run massive distribut systems uh including search Gmail and of course our public Cloud um but we couldn't just blindly use those Technologies uh for multiple reasons and the more importantly the the reason is because those Technologies are actually built for a very different scale so Google's internal infrastructure is quite literally built for a planning scale um but the good news is that um Google has invested in building open source variant of those internal Technologies uh over the years and so can kind of let us start small and kind of scale up so this is one of our key design kind of architecture goals all right so um this naturally leads us to the cloud native ecosystem so in cncf we have so many building blocks that we that we uh that we can can use to build a cloud for example of course you have kubernetes uh which is a very
