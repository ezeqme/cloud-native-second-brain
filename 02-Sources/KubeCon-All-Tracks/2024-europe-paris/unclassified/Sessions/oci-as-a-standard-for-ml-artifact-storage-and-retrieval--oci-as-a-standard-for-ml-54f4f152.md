---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["AI ML", "Storage Data"]
speakers: ["Peyman Norouzi", "Eric Koepfle", "Bloomberg"]
sched_url: https://kccnceu2024.sched.com/event/1YeLi/oci-as-a-standard-for-ml-artifact-storage-and-retrieval-peyman-norouzi-eric-koepfle-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=OCI+as+a+Standard+for+ML+Artifact+Storage+and+Retrieval+CNCF+KubeCon+2024
slides: []
status: parsed
---

# OCI as a Standard for ML Artifact Storage and Retrieval - Peyman Norouzi & Eric Koepfle, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: France / Paris
- Speakers: Peyman Norouzi, Eric Koepfle, Bloomberg
- Schedule: https://kccnceu2024.sched.com/event/1YeLi/oci-as-a-standard-for-ml-artifact-storage-and-retrieval-peyman-norouzi-eric-koepfle-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=OCI+as+a+Standard+for+ML+Artifact+Storage+and+Retrieval+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre OCI as a Standard for ML Artifact Storage and Retrieval.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeLi/oci-as-a-standard-for-ml-artifact-storage-and-retrieval-peyman-norouzi-eric-koepfle-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=OCI+as+a+Standard+for+ML+Artifact+Storage+and+Retrieval+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hGM5KQLzbYc
- YouTube title: OCI as a Standard for ML Artifact Storage and Retrieval - Peyman Norouzi & Eric Koepfle, Bloomberg
- Match score: 0.823
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/oci-as-a-standard-for-ml-artifact-storage-and-retrieval/hGM5KQLzbYc.txt
- Transcript chars: 35681
- Keywords: artifact, models, software, registry, process, platform, question, bloomberg, machine, learning, storage, around, deliver, actually, concepts, security, important, provide

### Resumo baseado na transcript

so my name is pan nzi uh I'm a product manager in the CTO organization at Bloomberg and today with me I have Eric hi I'm Eric kle a software engineer and the architect on the model registry we're going to be presenting and uh we're going to talk about Model Management um I'm going to cover some of the problems that we identify from Model Management and then Eric is going to cover how we came up with the solution and how oci plays A Part a core part

### Excerpt da transcript

so my name is pan nzi uh I'm a product manager in the CTO organization at Bloomberg and today with me I have Eric hi I'm Eric kle a software engineer and the architect on the model registry we're going to be presenting and uh we're going to talk about Model Management um I'm going to cover some of the problems that we identify from Model Management and then Eric is going to cover how we came up with the solution and how oci plays A Part a core part of that solution okay if you attended the keynote you probably have seen these slides a portion of it but uh I'm going to quickly go over what we do at Bloomberg Bloomberg is a technology company that provides uh software solutions for financial Professionals in the finance industry uh we one of our main products is called Bloomberg terminal uh and Bloomberg terminal provides many functionalities that allows users to get access to Raw Data Insights uh analytics tools and communication tools the scale of our operation is quite massive we process large chunk of data on a daily basis you can look at some of these numbers they're quite large and these are all daily numbers the amount of data we we process and because of this large amount of data that we process on a daily basis it's super important for this data to be structured in a way that is useful and digestible for our users and uh because of that AI you know recently there are a lot of hyper around AI large language models open AI but AI has been a big part of our product uh and big part of our culture we've been working on AI products for the past 15 years and uh since 2009 and because of this we have over 3 plus developers researchers that work on machine learning and they create and they have expertise in national language processing machine learning information retrieval search and uh they deliver uh products that allows us to deliver value through the Bloomberg terminal other products that Bloomberg has and internally we have a platform called the data science platform and the data science platform provides infrastructure that is optimized for machine learning use cases think gpus for training high performance Computing uh inference in the keynote we touched on some of these uh our colleague kind of went over those and we also provide services and tools uh that makes these infrastructure really use usable for our users to be able to do the whole process and deliver value with machine learning and they do this by going over model development life cycle I
