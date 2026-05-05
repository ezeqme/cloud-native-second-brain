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
themes: ["GitOps Delivery"]
speakers: ["Alan Clucas", "Lead"]
sched_url: https://kccnceu2026.sched.com/event/2EFxq/project-lightning-talk-argo-workflows-4-whats-new-and-whats-next-alan-clucas-lead
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Argo+Workflows+4%2C+What%27S+New+And+What%27S+Next+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Argo Workflows 4, What'S New And What'S Next - Alan Clucas, Lead

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[GitOps Delivery]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alan Clucas, Lead
- Schedule: https://kccnceu2026.sched.com/event/2EFxq/project-lightning-talk-argo-workflows-4-whats-new-and-whats-next-alan-clucas-lead
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Argo+Workflows+4%2C+What%27S+New+And+What%27S+Next+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Argo Workflows 4, What'S New And What'S Next.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFxq/project-lightning-talk-argo-workflows-4-whats-new-and-whats-next-alan-clucas-lead
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Argo+Workflows+4%2C+What%27S+New+And+What%27S+Next+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YbW24qbJ78I
- YouTube title: Project Lightning Talk: Argo Workflows 4, What's New And What's Next - Alan Clucas, Lead
- Match score: 0.963
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-argo-workflows-4-whats-new-and-whats-next/YbW24qbJ78I.txt
- Transcript chars: 4375
- Keywords: workflows, argo, workflow, engine, working, expressions, restart, probably, define, number, plugins, youtube, couple, hopefully, versions, started, tracing, github

### Resumo baseado na transcript

Um, you've probably heard of Argo in general, Argo Workflows is one of the sub projects. Um, and if you don't know what Argo Workflows does, it's a batch processing engine for uh, Kubernetes. Um the trade-off is you lose your pod isolation, but um that is the only way of fixing that problem.

### Excerpt da transcript

Hi. Um, you've probably heard of Argo in general, Argo Workflows is one of the sub projects. It's actually the oldest. Um, and if you don't know what Argo Workflows does, it's a batch processing engine for uh, Kubernetes. It's very Kubernetes native. It runs all of your steps in pods. Um, so you can define a series of pods as steps or a DAG and it orchestrates them and provides facilities for passing data between those pods. Um, that's the detail I'm going to be able to give you in five minutes. Um, because what I'm going to talk about is what we've done recently. Um, 4.0 came out earlier this year. It's got a number of new features on the screen. Um, artifact drivers are probably the biggest bit which is so you can write your own plugins to uh transport data in and out of those pods. Um, I did a whole talk on this about two hours ago. So, um, that will be on the Argoon YouTube site, um, in a couple of weeks, I imagine. Um, we've got, uh, full cell validation in our full CRDs. Up until about 3.7, our CRDs were very, very shrunk.

Um, and they are now very full. So hopefully, if you submit a workflow that really, really won't run, it'll tell you you've spelled stuff wrong and all of that kind of thing. Um, we've got, uh, in 3.6, Six, we introduced mult uh plural versions of a number of uh primitives and they have been removed in 4.0. The singular versions have and there's a new tool argo convert to help you um get updated to version 4. Um the uh controller will also restart pods that have never started. It's got a restart strategy. If what you're doing is your pod might be not um item potent that would be bad if we restarted it. But under these cases we do know we can restart it. So we we do that. Um already merge for 4.1 is workflows tracing. There's a QR code and a link to the YouTube talk on that done a couple of years ago. It's not that long. Um but this is tracing of the full workflow. Um working with CI/CD uh SEMCOM in open telemetry to help define what uh traces of this sort of size mean. They're they're working on GitHub.

You can get the same sort of thing out of GitHub now. Um but this is allow allows you to see how your workflow is using its time what bits are taking too long and you can you can also imp trace inside your workloads as well and that will become all part of one big trace. Um some future plans uh we've started working on reworking the DAG engine uh to separate it from the part that creates the pods so that they are we can do clever
