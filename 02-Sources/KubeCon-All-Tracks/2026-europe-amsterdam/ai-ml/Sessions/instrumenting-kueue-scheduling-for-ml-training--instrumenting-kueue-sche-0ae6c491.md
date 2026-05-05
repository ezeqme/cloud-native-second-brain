---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "AI + ML"
themes: ["AI ML"]
speakers: ["Amy Chen", "CoreWeave", "Gabriel Saba", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2CW0P/instrumenting-kueue-scheduling-for-ml-training-amy-chen-coreweave-gabriel-saba-google
youtube_search_url: https://www.youtube.com/results?search_query=Instrumenting+Kueue+Scheduling+for+ML+Training+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Instrumenting Kueue Scheduling for ML Training - Amy Chen, CoreWeave & Gabriel Saba, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Amy Chen, CoreWeave, Gabriel Saba, Google
- Schedule: https://kccnceu2026.sched.com/event/2CW0P/instrumenting-kueue-scheduling-for-ml-training-amy-chen-coreweave-gabriel-saba-google
- Busca YouTube: https://www.youtube.com/results?search_query=Instrumenting+Kueue+Scheduling+for+ML+Training+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Instrumenting Kueue Scheduling for ML Training.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW0P/instrumenting-kueue-scheduling-for-ml-training-amy-chen-coreweave-gabriel-saba-google
- YouTube search: https://www.youtube.com/results?search_query=Instrumenting+Kueue+Scheduling+for+ML+Training+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rcrl8-CudVw
- YouTube title: Instrumenting Kueue Scheduling for ML Training - Amy Chen, CoreWeave & Gabriel Saba, Google
- Match score: 0.782
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/instrumenting-kueue-scheduling-for-ml-training/rcrl8-CudVw.txt
- Transcript chars: 33021
- Keywords: cluster, workload, workloads, scheduling, guarantee, admission, actually, guarantees, fragmentation, resources, pending, priority, preeemption, violations, gpu, violation, issues, schedule

### Resumo baseado na transcript

Thank you so much for coming to our talk um titled instrumenting Q for machine learning training. My name is Amy and I'm a software engineer at Cororeweave and an upstream Q contributor. So large organizations for instance have cost centers, budgets, a lot of different financial models for how they're vending GPUs to underlying teams. So this opaque scheduling queuing process directly leads into a confusing um question where researchers often ask why isn't my workload scheduling practitioners of slurm for instance a scheduler that has been here way longer than Q um and that is over 20 years old also have problems answering this complex question. >> We'll start with an introduction to scheduling and illustrate how difficult of a problem it is. If resources were unlimited and free, this problem would be simple to solve.

### Excerpt da transcript

All right, let's get started. Hi everyone. Thank you so much for coming to our talk um titled instrumenting Q for machine learning training. My name is Amy and I'm a software engineer at Cororeweave and an upstream Q contributor. >> Hi, I'm Gabriel Saba. I'm a Google software engineer and a maintainer of Q. >> So for today our talk will start with briefly introducing the Q scheduling problem space and then we'll understand where Q fits as a batch scheduler and then after that we'll provide a highle overview of Q. So the reason why we're going through all this is because it's important to understand some concrete Q scheduling issues later in the talk and finally we'll offer a recipe to answer researchers when they ask why isn't my workload scheduling. So let's start off by chatting about the motivation for Q. Q is a batch job dispatcher. The reason why we need something like Q at all for machine learning training clusters is because compute is expensive and researchers need to split up GPU compute time in a reasonable way.

So if this hardware were cheap, each researcher could just sit on a bunch of capacity without worrying about whether that hardware is being used or not. Given these constraints, compute organizations really care about the percentage of utilization overall for the cluster. So you basically want as close to 100% utilization 24/7 as possible because again this stuff is expensive. Um in a large multi-tenant training environment, people really care about the GPUs they are vended. So large organizations for instance have cost centers, budgets, a lot of different financial models for how they're vending GPUs to underlying teams. However, using a batch dispatcher requires complex queuing, prioritization, and quota rules, which can be difficult to reason about, especially when you're trying to understand if there's scheduling bugs along the submission path. So this opaque scheduling queuing process directly leads into a confusing um question where researchers often ask why isn't my workload scheduling practitioners of slurm for instance a scheduler that has been here way longer than Q um and that is over 20 years old also have problems answering this complex question.

This is actually one of the most important questions for training cluster operators and one of the hardest questions to answer because of the many togglers all schedulers have. So, as platform operators, we need to be able to answer when a workload is expected to remain pending or
