---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Security + Identity + Policy"
themes: ["Security", "Kubernetes Core"]
speakers: ["Peter Kelly", "Tigera"]
sched_url: https://kccnceu2022.sched.com/event/ytrt/full-mesh-encryption-in-kubernetes-with-wireguard-and-calico-peter-kelly-tigera
youtube_search_url: https://www.youtube.com/results?search_query=Full+Mesh+Encryption+in+Kubernetes+with+WireGuard+and+Calico+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Full Mesh Encryption in Kubernetes with WireGuard and Calico - Peter Kelly, Tigera

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Peter Kelly, Tigera
- Schedule: https://kccnceu2022.sched.com/event/ytrt/full-mesh-encryption-in-kubernetes-with-wireguard-and-calico-peter-kelly-tigera
- Busca YouTube: https://www.youtube.com/results?search_query=Full+Mesh+Encryption+in+Kubernetes+with+WireGuard+and+Calico+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Full Mesh Encryption in Kubernetes with WireGuard and Calico.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytrt/full-mesh-encryption-in-kubernetes-with-wireguard-and-calico-peter-kelly-tigera
- YouTube search: https://www.youtube.com/results?search_query=Full+Mesh+Encryption+in+Kubernetes+with+WireGuard+and+Calico+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=G_jcvYMRUhc
- YouTube title: Full Mesh Encryption in Kubernetes with WireGuard and Calico - Peter Kelly, Tigera
- Match score: 0.943
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/full-mesh-encryption-in-kubernetes-with-wireguard-and-calico/G_jcvYMRUhc.txt
- Transcript chars: 29554
- Keywords: calico, cluster, configuration, encryption, public, encrypted, network, another, little, traffic, mesh, across, interface, actually, everything, around, couple, tunnel

### Resumo baseado na transcript

so uh thanks for coming to the talk today um just start with a little bit of background about about myself um and and then take you through what we're going to talk about today um so I work for tigera so tigera is the company behind project Calico um which is the most deployed cni for kubernetes um Powers about 2 million Nords daily in about 166 countries um igera is based in in the US but we have an office in Cork in Ireland as well which is of node B um and then it has a list of allowed IPS which represent um host Network pods which is the first IP and then the workload pods which are the other two IPS so you imagine is as you scale this out and

### Excerpt da transcript

so uh thanks for coming to the talk today um just start with a little bit of background about about myself um and and then take you through what we're going to talk about today um so I work for tigera so tigera is the company behind project Calico um which is the most deployed cni for kubernetes um Powers about 2 million Nords daily in about 166 countries um igera is based in in the US but we have an office in Cork in Ireland as well which is where I'm from um so it's been a nice treat to come to the sunshine in Valencia from Ireland um probably had too many AGA Dev valencias this week but it's been a great trip uh it's my first time speaking at cucon um it's actually my first time speaking in front of a group this big so please just just bear with me as we go through the the talk um my own background is in engineering software development um still technically involved in all of the the projects that we doing a tigera and contributing uh but not I'm not a security researcher so I'm not going to go deep into um ciphers and the type of uh cryptography that's being used by wire guard um but we will talk about some of some of that as we go through it okay so the goals today so we're going to talk a little bit about encryption as it stands in kubernetes um what are some of the popular options that people use currently um and why Calico decided to use wire guard so we'll recap a little bit about what Calico does we'll talk about uh wire guard and how it works and then how these mesh together to create a a fully encrypted uh cluster um we'll we'll we'll finish off talking about some gotches so we didn't get everything right when we when we implemented this feature um there's still things that we want to do in the future and and and look for uh contributors to help us to do that um and there's some some gaps as well that we can talk about so really the the the thing with the talk today is to to see this as a it's an alternative option to mtls with service mesh or IPC um one is not better or worse than the other there's pros and cons for for different encryption options in kubernetes but this is to present a different option especially if you're already using Calico as your cni so to kind of story with encryption in in kubernetes today what what we see when we talk to our our community our users uh the the kind of number one use case for for using encryption is is compliance actually uh whether it's PCI compliance or Hippa uh that's always the the top of the the to
