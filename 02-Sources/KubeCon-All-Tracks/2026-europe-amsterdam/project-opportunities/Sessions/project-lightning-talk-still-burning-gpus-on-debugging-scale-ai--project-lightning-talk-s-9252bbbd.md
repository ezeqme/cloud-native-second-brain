---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Anna Kramar", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyc/project-lightning-talk-still-burning-gpus-on-debugging-scale-ai-in-one-line-anna-kramar-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Still+Burning+GPUs+On+Debugging%3F+Scale+AI+In+One+Line+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Still Burning GPUs On Debugging? Scale AI In One Line - Anna Kramar, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Anna Kramar, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyc/project-lightning-talk-still-burning-gpus-on-debugging-scale-ai-in-one-line-anna-kramar-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Still+Burning+GPUs+On+Debugging%3F+Scale+AI+In+One+Line+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Still Burning GPUs On Debugging? Scale AI In One Line.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyc/project-lightning-talk-still-burning-gpus-on-debugging-scale-ai-in-one-line-anna-kramar-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Still+Burning+GPUs+On+Debugging%3F+Scale+AI+In+One+Line+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ix5kmLvlA5Y
- YouTube title: Project Lightning Talk: Still Burning GPUs On Debugging? Scale AI In One Line - Anna Kramar
- Match score: 1.006
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-still-burning-gpus-on-debugging-scale-ai-in-one/Ix5kmLvlA5Y.txt
- Transcript chars: 4151
- Keywords: training, function, client, distributed, workloads, config, change, already, recently, debugging, everyone, maintainer, instead, introducing, facing, locally, trainer, whenever

### Resumo baseado na transcript

Uh today I'm going to talk about how you can um make easier to run any AI workloads at any scale. So instead of just introducing the project to you uh let me start with introducing the problem that most data scientists are facing um and how we are solving it. For distributed training, we are skipping this part because we are using Kubernetes back end um as default and then we are providing um training function for both cases but also for distributed training we are providing the number of nodes and resources per node. Um you can also change it to the um containerized back end such as docker podman uh for your local development as well as whenever you're ready to scale it you can use kubernetes back end and you didn't need to change any um function or code in your training function you just changed one line and that's it. Uh also for model versioning and artifact storage you can use model registry client and we just recently added a spark client for and distributed data processing um on spark.

### Excerpt da transcript

Hi everyone. Uh today I'm going to talk about how you can um make easier to run any AI workloads at any scale. And with that my name is Ana Kmer. I'm a certifi engineer at Red Hat and I'm CFL SDK maintainer. So instead of just introducing the project to you uh let me start with introducing the problem that most data scientists are facing um and how we are solving it. So imagine you are building your training function and you run it locally. It works and now you need to scale it. you need to run it on Kubernetes and that's where you start facing all the infrastructure issues with pods, CRDs, YAML files. You need to debug your portuler and so on. So you end up spending a lot of your time on debugging instead of building or improving your AI model. Um, and every fail costs a lot of money because of the GPU hours you spent. So um is there a better way to run AI workloads uh on scale? There is. We are building Qflow SDK for that. So Qflow SDK is a set of unified pyonic APIs um to run any AI workloads at any scale.

You can access that with pip install Qflow. Um and let me show you how that works. So here's you have your training function and you can run it locally using trainer client um and then whenever you're ready you can scale it and distribute it across different GPUs uh with few modifications. So first of all for local execution mode we are using the backend config which is local process backend config. That means that your training function will be running as a subprocess. For distributed training, we are skipping this part because we are using Kubernetes back end um as default and then we are providing um training function for both cases but also for distributed training we are providing the number of nodes and resources per node. Uh so in total we are going to distribute our training function across 800 GPUs. So we just added a few lines and we needed we didn't need to make any modifications to our training function. Um so this is my favorite part is that you can change your environment variable really easily with just one line.

So as you seen for quick parting you can use the subprocess config. Um you can also change it to the um containerized back end such as docker podman uh for your local development as well as whenever you're ready to scale it you can use kubernetes back end and you didn't need to change any um function or code in your training function you just changed one line and that's it. Um so that's one of the cool features we have in the
