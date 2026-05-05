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
speakers: ["Eduardo Arango Gutierrez", "NVIDIA", "Ryan Zhang", "Microsoft"]
sched_url: https://kccnceu2024.sched.com/event/1YeOs/introducing-clusterinventory-and-clusterfeature-api-eduardo-arango-gutierrez-nvidia-ryan-zhang-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Introducing+ClusterInventory+and+ClusterFeature+API+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Introducing ClusterInventory and ClusterFeature API - Eduardo Arango Gutierrez, NVIDIA & Ryan Zhang, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Eduardo Arango Gutierrez, NVIDIA, Ryan Zhang, Microsoft
- Schedule: https://kccnceu2024.sched.com/event/1YeOs/introducing-clusterinventory-and-clusterfeature-api-eduardo-arango-gutierrez-nvidia-ryan-zhang-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Introducing+ClusterInventory+and+ClusterFeature+API+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Introducing ClusterInventory and ClusterFeature API.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOs/introducing-clusterinventory-and-clusterfeature-api-eduardo-arango-gutierrez-nvidia-ryan-zhang-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Introducing+ClusterInventory+and+ClusterFeature+API+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Xt1cuHKjKg8
- YouTube title: Introducing ClusterInventory and ClusterFeature API - Eduardo Arango Gutierrez & Ryan Zhang
- Match score: 0.819
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/introducing-clusterinventory-and-clusterfeature-api/Xt1cuHKjKg8.txt
- Transcript chars: 31405
- Keywords: cluster, multicluster, basically, application, actually, clusters, solutions, management, inventory, manager, feature, scheduling, already, infantry, projects, specific, trying, another

### Resumo baseado na transcript

hi everyone uh welcome to this presentation uh I'm excited to see so many people interested in boring stuff like defining apis so uh we try to keep this uh fresh and uh this is more about like welcoming everyone to the conversation we just want to build new apis to make things easier for multicluster so uh let's start by saying that defining apis is hard from the name itself so I think you all came to introducing inventory cluster and closer fishal API uh the names have gone

### Excerpt da transcript

hi everyone uh welcome to this presentation uh I'm excited to see so many people interested in boring stuff like defining apis so uh we try to keep this uh fresh and uh this is more about like welcoming everyone to the conversation we just want to build new apis to make things easier for multicluster so uh let's start by saying that defining apis is hard from the name itself so I think you all came to introducing inventory cluster and closer fishal API uh the names have gone to many iterations and there is actually a poll at the end of the presentation on where we are setting new names to the API so every time we run a Sig multicluster meeting we propose new names so welcome again to Cluster inventory and no feature group API talk uh it keeps changing so maybe at the end of this talk it's going to be a different name uh my name Carlos uh my quest speaker Ryan I'm from Nvidia he's from Microsoft and we will try to keep this light and interesting as possible uh who am I uh first time in real life cucon I I did presentations during pandemic but uh for those who never had seen me I've been around the container industry for like seven years or so and uh now we work at Nvidia at the cloud NY team basically trying to enable gpus into curetes and make things easier for all of you and uh Ryan hello uh my name is Ryan and this is also my first kubic Kon it's great that uh the first kuic Kon can get to talk to so many people here um who am I um I am currently working in asual kubernetes service I'm a principal SDM and in my previous life uh I worked on kuiva and oam as a founding member I don't know how many of you remember oam and uh and before that uh way before that I did a PhD in a qu Computing again I don't know how many of you know what good Computing is but uh that's not the point okay so today I'm going to talk about uh a multicluster and in this talk um we I'm going to first give you a brief history of multicluster and then I will present the motivations and then we are going to have some deep dive into the two apis that we are proposing and developing at the end there's a Q&A session um um before that uh let's do some data driven presentation um how many of you are working with kubernetes clusters um hands on oh oh great this is could become nice how many of you have only one cluster you can you can leave this is not talking for you but how many of you have 10 more than 10 wow still a lot 100 oh okay a thousand okay talk to me after after you you are my aud
