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
themes: ["AI ML", "Platform Engineering", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Alexis Bonnin", "Guillaume Maquinay", "Thales Aerospace"]
sched_url: https://kccnceu2024.sched.com/event/1YeQA/make-your-cluster-fly-embed-a-multi-node-kubernetes-cluster-inside-an-aircraft-using-puppet-flux-alexis-bonnin-guillaume-maquinay-thales-aerospace
youtube_search_url: https://www.youtube.com/results?search_query=Make+Your+Cluster+Fly%3A+Embed+a+Multi-Node+Kubernetes+Cluster+Inside+an+Aircraft+Using+Puppet+%26+Flux+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Make Your Cluster Fly: Embed a Multi-Node Kubernetes Cluster Inside an Aircraft Using Puppet & Flux - Alexis Bonnin & Guillaume Maquinay, Thales Aerospace

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Alexis Bonnin, Guillaume Maquinay, Thales Aerospace
- Schedule: https://kccnceu2024.sched.com/event/1YeQA/make-your-cluster-fly-embed-a-multi-node-kubernetes-cluster-inside-an-aircraft-using-puppet-flux-alexis-bonnin-guillaume-maquinay-thales-aerospace
- Busca YouTube: https://www.youtube.com/results?search_query=Make+Your+Cluster+Fly%3A+Embed+a+Multi-Node+Kubernetes+Cluster+Inside+an+Aircraft+Using+Puppet+%26+Flux+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Make Your Cluster Fly: Embed a Multi-Node Kubernetes Cluster Inside an Aircraft Using Puppet & Flux.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQA/make-your-cluster-fly-embed-a-multi-node-kubernetes-cluster-inside-an-aircraft-using-puppet-flux-alexis-bonnin-guillaume-maquinay-thales-aerospace
- YouTube search: https://www.youtube.com/results?search_query=Make+Your+Cluster+Fly%3A+Embed+a+Multi-Node+Kubernetes+Cluster+Inside+an+Aircraft+Using+Puppet+%26+Flux+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WWSMNHXJAIc
- YouTube title: Make Your Cluster Fly: Embed a Multi-Node Kubernetes Cluster Inside an Aircraft Using Puppet & Flux
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/make-your-cluster-fly-embed-a-multi-node-kubernetes-cluster-inside-an/WWSMNHXJAIc.txt
- Transcript chars: 28577
- Keywords: registry, cluster, create, flux, available, aircraft, access, actually, images, connectivity, container, onboard, cannot, solution, resources, operator, ground, deploy

### Resumo baseado na transcript

hello everybody okay thank you for coming this is the last thought of the day so thank you for coming okay so I'm g m I'm a software architect working for Tales and I am Alex and I'm also a software architect at Tales so we are both working with our buddies here uh on this kind of product this is a big picture of the product so as you can see uh on the top here you have this data center that is also on this table that you

### Excerpt da transcript

hello everybody okay thank you for coming this is the last thought of the day so thank you for coming okay so I'm g m I'm a software architect working for Tales and I am Alex and I'm also a software architect at Tales so we are both working with our buddies here uh on this kind of product this is a big picture of the product so as you can see uh on the top here you have this data center that is also on this table that you can also see at the Talis boo k34 right okay and okay so thanks to this data center onboard data center that we call surprisingly ODC um we can run different kind of workloads on board so depending on your use case could be connected to different equipments notably the the cabin could be seatbacks it could be a access point serving for personal electric device devices electronic devices it can be uh connected to the connectivity um and that's pretty much it this data center itself as a edge part is connected to the ground platform through the through the satcom so either satcom or when we are on ground we have the four 5G or 4G connectivity and this platform uh provides with a PO for all the stakeholders so Airlines uh third parties as stus we also operate via this this portal so when we started to work on this project uh was in 2020 uh so we had this top four tasks to tackle so obviously the hardware the big part so we I'm I'm glad I don't I don't do a hardware because they had a great challenge to to face um we they have to comply with the DU 160 which is environment constraints um and just to give you a bit of idea this wall box only consumes 300 watts so technically it's a not more than a hair dryer uh yeah and PO is one thing but cooling is another and this is one of the biggest challenges as well you have to make be able to cool this stuff and sometimes temperatures grows very high especially when you're on Middle eist on the T mark so it can be a big deal once you have the hardware you bring on top the the software so with my team we were working on especially the the lowest part of the software so being able between the hardware bring the OS on top of it be able to deploy the OS over the year uh there are various topics provision provisioning is part of it um and as we wanted to assemble the current communities cluster on that we obviously had a a team working on the the grand infrastructure this is a big part but but that we won't cover today and we have of course services that we want to bring uh on this in this system that can
