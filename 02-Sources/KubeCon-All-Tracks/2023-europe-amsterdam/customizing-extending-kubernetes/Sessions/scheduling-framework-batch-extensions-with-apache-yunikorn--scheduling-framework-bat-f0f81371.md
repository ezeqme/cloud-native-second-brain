---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Wilfred Spiegelenburg", "Peter Bacsko", "Cloudera"]
sched_url: https://kccnceu2023.sched.com/event/1Hydt/scheduling-framework-batch-extensions-with-apache-yunikorn-wilfred-spiegelenburg-peter-bacsko-cloudera
youtube_search_url: https://www.youtube.com/results?search_query=Scheduling+Framework%3A+Batch+Extensions+with+Apache+YuniKorn+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Scheduling Framework: Batch Extensions with Apache YuniKorn - Wilfred Spiegelenburg & Peter Bacsko, Cloudera

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Wilfred Spiegelenburg, Peter Bacsko, Cloudera
- Schedule: https://kccnceu2023.sched.com/event/1Hydt/scheduling-framework-batch-extensions-with-apache-yunikorn-wilfred-spiegelenburg-peter-bacsko-cloudera
- Busca YouTube: https://www.youtube.com/results?search_query=Scheduling+Framework%3A+Batch+Extensions+with+Apache+YuniKorn+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Scheduling Framework: Batch Extensions with Apache YuniKorn.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hydt/scheduling-framework-batch-extensions-with-apache-yunikorn-wilfred-spiegelenburg-peter-bacsko-cloudera
- YouTube search: https://www.youtube.com/results?search_query=Scheduling+Framework%3A+Batch+Extensions+with+Apache+YuniKorn+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ij2UQ9V4CBU
- YouTube title: Scheduling Framework: Batch Extensions with Apache YuniKorn - Wilfred Spiegelenburg & Peter Bacsko
- Match score: 0.848
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/scheduling-framework-batch-extensions-with-apache-yunikorn/ij2UQ9V4CBU.txt
- Transcript chars: 28042
- Keywords: scheduling, priority, unicorn, application, running, cluster, within, scheduler, quotas, resources, resource, schedule, whatever, default, applications, queues, guaranteed, preemption

### Resumo baseado na transcript

good afternoon Wilfred spiegelenburg and Peter bashco here we're part of the PMC unique arpeggio unicorn group designed the Apache unicorn from scratch I've been doing Apache unicorn since Inception about three years ago and Peter hi my name is Peter rochko I joined Club there in 2016. we worked on Uzi Hadoop my produced yarn and then joined the nuclear team in 2021. the scheduling decisions the only way that has changed between what we do with the plugin and the Divo mode is the way that we interact with kubernetes and what we need to do ourselves and what the default scheduler does for us yeah the not be scheduled yet the default scheduler had already looked at and marked as unscheduled and then the auto scaler kicks in and says hey I'm I need a new note because this is remarked as unschedule so that's why the the pre and Q

### Excerpt da transcript

good afternoon Wilfred spiegelenburg and Peter bashco here we're part of the PMC unique arpeggio unicorn group designed the Apache unicorn from scratch I've been doing Apache unicorn since Inception about three years ago and Peter hi my name is Peter rochko I joined Club there in 2016. we worked on Uzi Hadoop my produced yarn and then joined the nuclear team in 2021. so what we're going to talk about today is how we are using the schedule framework to give you some batch extensions in the kubernetes environment so like we said we're coming out of the Hep Hadoop yarn area so batch processing large data processing and we're trying to give you the similar kinds of things within the setup around kubernetes so what are the things that we're looking at when when we look at scheduling on on kubernetes we want to do workload queuing when when batches gets deployed when batches get generated we generate often or one in one go we want to keep them around we want to start them whenever things will um or need to be run we want to do an all-in-one kind of scheduling setup gang scheduling we don't spawn up one pot we want to do a set of pods which one is a driver other side of workers spark is a is a good example for that but there's other pie torch uh imp there's a number of things that will do that for you things that are not available in instantly the other um extra bit that we want to give you is application sorting so instead of looking at just one pot or a job or a demon set with another there's a mixture of bots a group of bots that together for the application we want to schedule based on the requests that come from from that thing it could be one pot to begin with scale up to a thousand parts and then drop down again to a couple of pots like what we do with data processing at the point in time that we need it we scale up the pods we do what we need to do and the pots go away so we've got a real bursty kind of a deployment but we we still want to see all these Bots being scheduled as part of one thing not every single port separately so these kinds of schedulers these kinds of facilities are there when you look at high performance product HPC pros and the batch processing when you come from a slurm or a yarn kind of setup yeah these same kind of things we're going to do or we want to do from Apache unicorn within kubernetes but kubernetes from its Origins was always a Services based setup we want to do both at the same time there's a number of schedulers that wi
