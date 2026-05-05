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
themes: ["AI ML", "Platform Engineering", "Kubernetes Core"]
speakers: ["Jago Macleod", "Google"]
sched_url: https://kccncna2024.sched.com/event/1i7pg/kubernetes-upgrades-less-pain-more-gain-and-maybe-a-little-swearing-jago-macleod-google
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Upgrades%3A+Less+Pain%2C+More+Gain+%28and+Maybe+a+Little+Swearing%29+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes Upgrades: Less Pain, More Gain (and Maybe a Little Swearing) - Jago Macleod, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Jago Macleod, Google
- Schedule: https://kccncna2024.sched.com/event/1i7pg/kubernetes-upgrades-less-pain-more-gain-and-maybe-a-little-swearing-jago-macleod-google
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Upgrades%3A+Less+Pain%2C+More+Gain+%28and+Maybe+a+Little+Swearing%29+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes Upgrades: Less Pain, More Gain (and Maybe a Little Swearing).

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pg/kubernetes-upgrades-less-pain-more-gain-and-maybe-a-little-swearing-jago-macleod-google
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Upgrades%3A+Less+Pain%2C+More+Gain+%28and+Maybe+a+Little+Swearing%29+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=e-6NCccsfO8
- YouTube title: Kubernetes Upgrades: Less Pain, More Gain (and Maybe a Little Swearing) - Jago Macleod, Google
- Match score: 0.95
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-upgrades-less-pain-more-gain-and-maybe-a-little-swearing/e-6NCccsfO8.txt
- Transcript chars: 31941
- Keywords: version, upgrade, release, cluster, clusters, upgrades, actually, important, interesting, versions, channel, working, support, compatibility, running, concept, features, better

### Resumo baseado na transcript

hi everybody we're coming into the final stretch here appreciate you showing up um hi so we're going to talk about kubernetes upgrades today in various parts uh first part I'm going to make a pretty concerted effort to convince you that you should want to upgrade frequently even if you don't think you do uh and explain why I think that's really important uh and then we're going to go into how to do that uh safely today and where we're going in the future uh so for introduction

### Excerpt da transcript

hi everybody we're coming into the final stretch here appreciate you showing up um hi so we're going to talk about kubernetes upgrades today in various parts uh first part I'm going to make a pretty concerted effort to convince you that you should want to upgrade frequently even if you don't think you do uh and explain why I think that's really important uh and then we're going to go into how to do that uh safely today and where we're going in the future uh so for introduction I'm jgo McLoud I lead open source kubernetes at Google uh and I work on gke especially in the upgrades space and also in the node area um so whenever customers have challenges uh I end up talking to those customers if you're some of those customers thank you uh it's wonderful to see you here uh all right we're going to see if this works look at that is amazing uh okay so this uh envelope this shape is amazing to me uh we used it a long time ago in a scalability talk um to talk about how challenging it is to scale kubernetes and how if you go up in one dimension you have to go down in another um part of the complexity in upgrades is that everything is expanding in every dimension I talked about running uh kubernetes 65,000 node clusters today and we also run on two nodes in retail environments uh Linux does similar scaling but they don't run the same binaries in both of those locations uh so it's pretty interesting uh and my ultimate fear is that we end up like a spork where it's kind of like a combination spoon fork and it doesn't really do anything very well uh and so this is my timate fear so we have to be really careful uh kubernetes has some advantages it's modular it has an extensible API there's some benefits uh that make this not an unwinable battle but it's something we have to focus on to do well so critically counterintuitively slowing down is counterproductive uh this is like riding a bike uh you're scared to ride a bike you slow down you will tip over and you will skin your knee uh it is takes some getting used to especially if you're coming from a more Legacy system where your upgrades or migrations are move it to the new version spend months or years fiddling with things hopefully you avoided the might as well project from hell where you might as well do this and that and the other thing while you're upgrading and migrating then you get everything just right and then nobody touch anything um this is not that world and so we're going to walk through why we have a core va
