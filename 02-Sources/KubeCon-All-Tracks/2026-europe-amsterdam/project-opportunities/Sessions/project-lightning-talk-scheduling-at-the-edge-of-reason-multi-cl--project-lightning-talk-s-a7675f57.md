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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["August Simonelli", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFxn/project-lightning-talk-scheduling-at-the-edge-of-reason-multi-cluster-ai-ocm-august-simonelli-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Scheduling+at+the+Edge+of+Reason%3A+Multi-Cluster+AI+%26+OCM+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Scheduling at the Edge of Reason: Multi-Cluster AI & OCM - August Simonelli, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: August Simonelli, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFxn/project-lightning-talk-scheduling-at-the-edge-of-reason-multi-cluster-ai-ocm-august-simonelli-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Scheduling+at+the+Edge+of+Reason%3A+Multi-Cluster+AI+%26+OCM+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Scheduling at the Edge of Reason: Multi-Cluster AI & OCM.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFxn/project-lightning-talk-scheduling-at-the-edge-of-reason-multi-cluster-ai-ocm-august-simonelli-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Scheduling+at+the+Edge+of+Reason%3A+Multi-Cluster+AI+%26+OCM+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Pbi3LD4I3BM
- YouTube title: Project Lightning Talk: Scheduling at the Edge of Reason: Multi-Cluster AI & OCM - August Simonelli
- Match score: 0.979
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-scheduling-at-the-edge-of-reason-multi-cluster/Pbi3LD4I3BM.txt
- Transcript chars: 5308
- Keywords: cluster, management, placement, scoring, learning, add-on, scheduling, dynamic, federated, clusters, whatever, multicluster, framework, constantly, basically, exciting, excited, everyone

### Resumo baseado na transcript

Um before I start I have a question and I think it's obvious from what we've just seen in the sessions but um who manages more than one cluster right and who manages more than one type of cluster? So the main thing I want to convey here about open cluster management is that it's multicluster and that we should all be thinking multicluster. Um what we're doing is using the OCM hub as the aggregator to help solve the high egress costs of doing training logic at the edge. So that handles that and then we abstract the orchestration into a federated learning CRD that reconciles the state into a manifest work. Basically it takes all your federated learning logic and turns it into open cluster management logic which is just uh just placement. So you can do that work out on the edge without all the extra um without all the extra challenges.

### Excerpt da transcript

Hello everyone. Um before I start I have a question and I think it's obvious from what we've just seen in the sessions but um who manages more than one cluster right and who manages more than one type of cluster? Yeah. Okay. So it's most of you. So the main thing I want to convey here about open cluster management is that it's multicluster and that we should all be thinking multicluster. You're hearing talks from everyone about that kind of stuff. So that's good. Today we're going to talk about a few features from open cluster management. That's dynamic scoring, an update on federated learning and some project updates. Okay, dynamic scoring is a framework framework for automating resource management on the fly from your metrics. So think of it this way. We deploy agents to the to the clusters, right? And these are deployed as an add-on. The agents then gather data from the clusters or from an external source. So you can feed this in and that is sent to a scoring API. You bring the scoring API, we give you logic on how to build it.

That is going to constantly evaluate metrics based on whatever you want to use. So I do have a demo. You can visit us in the project pavilion for that demo. Um essentially what that does is create placement and placement decisions inside of open cluster management. So this is happening constantly in the background. whatever logic you want to evaluate on it will go ahead and put that together and create this placement. What does that mean as a user? As you can see up here, you have a workload you want to deploy. You send that to an orchestrator which is then reading the placement. And again, the placement is constantly dynamically updating. So you might have an LLM backing it or some other fancy piece of logic, whatever you want to do. Um, and then that allows you to send the workloads down to the clusters. It's a simple concept, but it makes it very easy to use um and to very simply do dynamic uh placement. All right, next thing I want to talk about is federated learning. Um what we're doing is using the OCM hub as the aggregator to help solve the high egress costs of doing training logic at the edge.

So we've used a flower add-on in the beginning here. Um and that helps to automate the super node life cycle. Basically, it's an add-on. So an add-on in open cluster management is a way of easily deploying software to all your managed clusters. So that handles that and then we abstract the orchestration into a federated learning C
