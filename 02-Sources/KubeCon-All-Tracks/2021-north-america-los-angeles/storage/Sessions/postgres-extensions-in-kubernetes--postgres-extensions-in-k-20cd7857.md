---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Storage"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Álvaro Hernández", "OnGres"]
sched_url: https://kccncna2021.sched.com/event/lV1u/postgres-extensions-in-kubernetes-alvaro-hernandez-ongres
youtube_search_url: https://www.youtube.com/results?search_query=Postgres+Extensions+in+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Postgres Extensions in Kubernetes - Álvaro Hernández, OnGres

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Álvaro Hernández, OnGres
- Schedule: https://kccncna2021.sched.com/event/lV1u/postgres-extensions-in-kubernetes-alvaro-hernandez-ongres
- Busca YouTube: https://www.youtube.com/results?search_query=Postgres+Extensions+in+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Postgres Extensions in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV1u/postgres-extensions-in-kubernetes-alvaro-hernandez-ongres
- YouTube search: https://www.youtube.com/results?search_query=Postgres+Extensions+in+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hCp6p-0cxco
- YouTube title: Postgres Extensions in Kubernetes - Álvaro Hernández, OnGres
- Match score: 0.822
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/postgres-extensions-in-kubernetes/hCp6p-0cxco.txt
- Transcript chars: 27163
- Keywords: extensions, extension, postgres, database, phosphorus, available, cluster, container, controller, installed, version, install, mechanism, allows, number, source, loading, called

### Resumo baseado na transcript

hello everybody and welcome to this talk on kubecon cloud nativecon about postgres extensions in kubernetes in this talk i would like to introduce a novel mechanism built into an open source project to allow dynamic loading of postgres extensions in kubernetes this is a very noble way that enables to run any extension that you may want to run in again kubernetes so first about myself who am i you can just get to the slide but uh basically i am the ceo and founder of company called ongress

### Excerpt da transcript

hello everybody and welcome to this talk on kubecon cloud nativecon about postgres extensions in kubernetes in this talk i would like to introduce a novel mechanism built into an open source project to allow dynamic loading of postgres extensions in kubernetes this is a very noble way that enables to run any extension that you may want to run in again kubernetes so first about myself who am i you can just get to the slide but uh basically i am the ceo and founder of company called ongress congress means on postgres and that's pretty much everything that we do i've been myself a postgres dba developer application developer for more than 20 years and i'd like to specially specifically focus on r d on databases specifically podcast i also like to speak at postgres and all the types of conferences online uh actually i have to say that this is my first talk at cubecon i've tried four times before i've been rejected so i'm very happy to finally made it finally uh very happy to be here with you so let's look at phosphorus extension let me do a one on one and pause for sectioning extensions in case you're not familiar with them so postgres extensions you can think of them as the plugins of a browser right there they're software bundles that you may install that enhance the browser functionality so postgres extensions are pretty much the same but apply to a postgres database they extend the function the database in so many ways as we shall see they are actually one of the most often cited uh best features of possible so when someone speaks about phosphorus very early on the discussion say extensions are one of the very best things of phosphorus because actually they transform phosphorus they significantly augment the phosphorus functionality and make it a very adaptable and rich database what is also important about extensions is that they do not follow the yearly cuttings release cycle of postgres new features come to posters only once a year so if you want to develop new features and you pack them as extensions you'll be able to deliver these features to your users any moment and so that's why they are normally developed by third parties the extensions are also important for the ecosystem because they have prevented many uh forks of phosphorus because if you can run everything as all your functionality as an extension this is often the case then you don't need to fork phosphorus and it's just something that built on top of postgres and can run on top of any exist
