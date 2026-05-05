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
speakers: ["Yao Lin", "Reinhard Tartler", "Bloomberg"]
sched_url: https://kccnceu2024.sched.com/event/1YeLy/bloombergs-journey-to-a-multi-cluster-workflow-orchestration-platform-yao-lin-reinhard-tartler-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Bloomberg%27s+Journey+to+a+Multi-Cluster+Workflow+Orchestration+Platform+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Bloomberg's Journey to a Multi-Cluster Workflow Orchestration Platform - Yao Lin & Reinhard Tartler, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Yao Lin, Reinhard Tartler, Bloomberg
- Schedule: https://kccnceu2024.sched.com/event/1YeLy/bloombergs-journey-to-a-multi-cluster-workflow-orchestration-platform-yao-lin-reinhard-tartler-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Bloomberg%27s+Journey+to+a+Multi-Cluster+Workflow+Orchestration+Platform+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Bloomberg's Journey to a Multi-Cluster Workflow Orchestration Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeLy/bloombergs-journey-to-a-multi-cluster-workflow-orchestration-platform-yao-lin-reinhard-tartler-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Bloomberg%27s+Journey+to+a+Multi-Cluster+Workflow+Orchestration+Platform+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ntSGFk0290w
- YouTube title: Bloomberg's Journey to a Multi-Cluster Workflow Orchestration Platform - Yao Lin & Reinhard Tartler
- Match score: 0.927
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/bloombergs-journey-to-a-multi-cluster-workflow-orchestration-platform/ntSGFk0290w.txt
- Transcript chars: 26792
- Keywords: cluster, resources, workflow, database, workflows, argo, static, server, center, platform, actually, clusters, bloomberg, resource, management, generally, requirements, decisions

### Resumo baseado na transcript

hello my name is Rina tartler and this is yaolin and we welcome you to our presentation Bloomberg's journey to a multicluster workl orchestration platform let me start by giving you a little background about what we are working on we are part of the cloud native compute Services Group at Bloomberg where we offer a platform called workfl orchestration this is not an externally visible product which means that all of our customers are internal Engineers who generally use Bloomberg infrastructure and data the teamon system is rather new

### Excerpt da transcript

hello my name is Rina tartler and this is yaolin and we welcome you to our presentation Bloomberg's journey to a multicluster workl orchestration platform let me start by giving you a little background about what we are working on we are part of the cloud native compute Services Group at Bloomberg where we offer a platform called workfl orchestration this is not an externally visible product which means that all of our customers are internal Engineers who generally use Bloomberg infrastructure and data the teamon system is rather new but has seen quite rapid growth in popularity we believe that our requirements challenges and conclusions May resonate with at least some of you in the audience and we are thrilled to share with you what makes our journey unique and get into a conversation with you afterwards before we dive into the technical details let me walk you through what we mean with workfl orchestration platform to give you a better idea about what we're actually offering in a nutshell our work orchestration platform provides General utility compute for run to completion bad jobs so what does that mean specifically that means that our customers come to us with two things coding containers on our company's internal container registry and an execution plan that defi that defines in what poorts to execute in what order that plan may also decide on uh about fan out of branches of execution are defined find synchronization points where the workflow requires several nodes to terminate before proceeding luckily we are able to use argu workflows a cncf project that has reached the graduated maturity level in December 2022 for the core functionality that our clients primarily use Argo workflows comes with a controller custom resource definitions crds for Dax workflow steps and most prominently a user interface that allows users to visually observe the progression of their workflows it is also critical for debugging when containers don't execute as expected at Bloomberg we are proud to offer workflow orchestration as a service for a number of different use cases such as machine learning orchestration which covers training and tuning of our AI company's AI models as an aside AI is not something new to us at Bloomberg we've been using AI for more than 15 years since 2009 to manage the large volume of financial data news and analytics our customers access every single day now back to our system so we have users Implement custom cicd res Solutions in many cases we
