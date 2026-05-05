---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Research + Academia + HPC + Advanced Concepts"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Michał Woźniak", "Google", "Vanessa Sochat", "Lawrence Livermore National Laboratory"]
sched_url: https://kccnceu2023.sched.com/event/1HyaG/enabling-hpc-and-ml-workloads-with-the-latest-kubernetes-job-features-michal-wozniak-google-vanessa-sochat-lawrence-livermore-national-laboratory
youtube_search_url: https://www.youtube.com/results?search_query=Enabling+HPC+and+ML+Workloads+with+the+Latest+Kubernetes+Job+Features+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Enabling HPC and ML Workloads with the Latest Kubernetes Job Features - Michał Woźniak, Google & Vanessa Sochat, Lawrence Livermore National Laboratory

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Research + Academia + HPC + Advanced Concepts]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Michał Woźniak, Google, Vanessa Sochat, Lawrence Livermore National Laboratory
- Schedule: https://kccnceu2023.sched.com/event/1HyaG/enabling-hpc-and-ml-workloads-with-the-latest-kubernetes-job-features-michal-wozniak-google-vanessa-sochat-lawrence-livermore-national-laboratory
- Busca YouTube: https://www.youtube.com/results?search_query=Enabling+HPC+and+ML+Workloads+with+the+Latest+Kubernetes+Job+Features+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Enabling HPC and ML Workloads with the Latest Kubernetes Job Features.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyaG/enabling-hpc-and-ml-workloads-with-the-latest-kubernetes-job-features-michal-wozniak-google-vanessa-sochat-lawrence-livermore-national-laboratory
- YouTube search: https://www.youtube.com/results?search_query=Enabling+HPC+and+ML+Workloads+with+the+Latest+Kubernetes+Job+Features+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rGOT-1SiZtU
- YouTube title: Enabling HPC & ML Workloads with the Latest Kubernetes Job Features- Michał Woźniak & Vanessa Sochat
- Match score: 0.878
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/enabling-hpc-and-ml-workloads-with-the-latest-kubernetes-job-features/rGOT-1SiZtU.txt
- Transcript chars: 27540
- Keywords: flux, operator, cluster, create, vanessa, questions, policy, environment, simulation, actually, resource, features, portfolio, devices, resources, working, multiple, include

### Resumo baseado na transcript

okay I think we can we can start um so let me introduce myself I'm my name is Mikhail I'm a software engineer working for Google in the GK batch team and today I'm going to co-present with Vanessa from Lawrence Livermore National Laboratory who unfortunately cannot be with me on the stage but um I will play her part and she will be later for your questions on the slack so let me begin with a little bit of History like all of you now like kubernetes was built

### Excerpt da transcript

okay I think we can we can start um so let me introduce myself I'm my name is Mikhail I'm a software engineer working for Google in the GK batch team and today I'm going to co-present with Vanessa from Lawrence Livermore National Laboratory who unfortunately cannot be with me on the stage but um I will play her part and she will be later for your questions on the slack so let me begin with a little bit of History like all of you now like kubernetes was built originally with um with the focus on Long running and stateless applications and naturally there was a lot of feature gaps in the early job API to run batch workloads and but over the years users who wanted to use batch were still very determined to run batch on kubernetes even at the cost of worker runs of or re-implementing features which should have been provided by the call kubernetes but this leads to a lot of fragmentation in the in the ecosystem of batch so um we would like to improve the situation and reduce the fragmentation so that's why we started the batch working group initiative and we work under its umbrella to bring all the necessary features and Primitives to the Core kubernetes so we believe that this will improve workload profitability between different Frameworks and between different Cloud providers and also this will allow framework developers to focus on the value added rather than the implementation of the core functionality okay so let's take a look at what has been done on that front so here you can see on the left the list of problems and on the right the list of new features that address these problems in the recent releases of kubernetes so the list and go passes many areas you can see for example improved handling of periodic jobs or the job suspense field which is a stepping stone for job queuing something that Aldo talked at length but in this talk I would like to focus on two features that is index job and portfolio policy um so let me first introduce index job by the use case of processing a large data set so if we have a large data set we naturally want to split it into smaller chunks and process the data set in parallel by multiple workers in the world of kubernetes represented by parts but the problem in the early API and like the recommended approach was to create and maintain your own queue of tasks however if the data set isn't changing that we can do have a simpler solution and just assign the specific check of the data set based on the worker index and this is
