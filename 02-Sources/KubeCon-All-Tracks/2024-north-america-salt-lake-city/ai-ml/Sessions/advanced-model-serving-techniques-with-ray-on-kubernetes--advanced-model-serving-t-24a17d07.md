---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Andrew Sy Kim", "Google", "Kai-Hsun Chen", "Anyscale"]
sched_url: https://kccncna2024.sched.com/event/1i7kg/advanced-model-serving-techniques-with-ray-on-kubernetes-andrew-sy-kim-google-kai-hsun-chen-anyscale
youtube_search_url: https://www.youtube.com/results?search_query=Advanced+Model+Serving+Techniques+with+Ray+on+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Advanced Model Serving Techniques with Ray on Kubernetes - Andrew Sy Kim, Google & Kai-Hsun Chen, Anyscale

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Andrew Sy Kim, Google, Kai-Hsun Chen, Anyscale
- Schedule: https://kccncna2024.sched.com/event/1i7kg/advanced-model-serving-techniques-with-ray-on-kubernetes-andrew-sy-kim-google-kai-hsun-chen-anyscale
- Busca YouTube: https://www.youtube.com/results?search_query=Advanced+Model+Serving+Techniques+with+Ray+on+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Advanced Model Serving Techniques with Ray on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7kg/advanced-model-serving-techniques-with-ray-on-kubernetes-andrew-sy-kim-google-kai-hsun-chen-anyscale
- YouTube search: https://www.youtube.com/results?search_query=Advanced+Model+Serving+Techniques+with+Ray+on+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mASxYpfWUNU
- YouTube title: Advanced Model Serving Techniques with Ray on Kubernetes - Andrew Sy Kim & Kai-Hsun Chen
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/advanced-model-serving-techniques-with-ray-on-kubernetes/mASxYpfWUNU.txt
- Transcript chars: 37528
- Keywords: inference, gpu, support, serving, pretty, models, cluster, together, resource, important, performance, online, output, machine, second, memory, record, multiple

### Resumo baseado na transcript

Welcome to our talk we're going to be covering um Advanced model serving techniques with uh Ray and kubernetes um so yeah uh let's start with some quick intros I'm Andrew Sim I'm a software engineer at Google working on um gke and I've been um contributing to maintaining to uh the kubernetes project for several years and in various areas um and more recently I've been um uh maintaining the cuate project with kaisen and helping um Google Cloud customers uh build modern machine learning platforms right yeah uh then the community also offers the two deployment Solutions one is for kubernetes and the other one is for the virtual machines and the official solution for ran kubernetes in the open source Community is a CRA yeah and then uh why Ray is so is great with the exclamation point uh and then it returns uh a label which in this case is positive and a score of 99 uh so yeah racer makes it easy to scale out to multimodel deployments so specifically here we have an example

### Excerpt da transcript

Welcome to our talk we're going to be covering um Advanced model serving techniques with uh Ray and kubernetes um so yeah uh let's start with some quick intros I'm Andrew Sim I'm a software engineer at Google working on um gke and I've been um contributing to maintaining to uh the kubernetes project for several years and in various areas um and more recently I've been um uh maintaining the cuate project with kaisen and helping um Google Cloud customers uh build modern machine learning platforms right yeah uh hi everyone my name is kin Chan I am a software engineer in N scale N scale is a creator of Ray and I'm in a rord te and I'm maintain cubre project and contribute to like a Rec paragraphs and sound record stuff I think oh yeah uh I think AI is all around you that in today's life so uh when you te and Uber browse Tik Tok listen to music on Spotify discuss current events on r and watch video on Netflix you all have already intera with the AI build using Ray so for scanting AI workload Ray is almost everywhere yeah so what is Ray uh when we start to introduce Ray we should start from the fundamental uh the record uh when we program on a laptop we need to the program consist of the three elements you need to Define function you need to design a class and then you need to Define a variable and the R cor provides the distributed API that is one and one mapping with the three elements the red test is the remote function and re actor is a remote class and the ray object is the remote variable uh which means that when you submit a ray application across the cluster it will launch this class a function and a variable across the cluster and they can interact with each other and you don't need to worry uh which uh where is this like a function class variable is running on which note yeah so this means that it's pretty easy to convert your Python program into a distributed program because the pattern is PR very similar and the record goal is to make users programing a distribut system as if they were working on their laptop yeah so the record toen is like the infinite laptop yeah and uh uh this is a very simple record example uh first uh you just you need to add an annotation on the function uh so to declare that this function is a red task and then you call the f.

remote and it will create a red T in the in the rain node and it will return a nonblocking future uh finally you can Cod the R.G to get the final results from the cluster and you can see like it's a pre
