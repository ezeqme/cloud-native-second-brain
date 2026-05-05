---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Emerging + Advanced"
themes: ["Emerging + Advanced"]
speakers: ["Raulian-Ionut Chiorescu", "Hannes Hansen", "CERN"]
sched_url: https://kccnceu2026.sched.com/event/2CW1u/the-shell-awakens-cloud-native-workflows-for-particle-physicists-raulian-ionut-chiorescu-hannes-hansen-cern
youtube_search_url: https://www.youtube.com/results?search_query=The+Shell+Awakens%3A+Cloud+Native+Workflows+for+Particle+Physicists+CNCF+KubeCon+2026
slides: []
status: parsed
---

# The Shell Awakens: Cloud Native Workflows for Particle Physicists - Raulian-Ionut Chiorescu & Hannes Hansen, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Emerging + Advanced]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Raulian-Ionut Chiorescu, Hannes Hansen, CERN
- Schedule: https://kccnceu2026.sched.com/event/2CW1u/the-shell-awakens-cloud-native-workflows-for-particle-physicists-raulian-ionut-chiorescu-hannes-hansen-cern
- Busca YouTube: https://www.youtube.com/results?search_query=The+Shell+Awakens%3A+Cloud+Native+Workflows+for+Particle+Physicists+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre The Shell Awakens: Cloud Native Workflows for Particle Physicists.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW1u/the-shell-awakens-cloud-native-workflows-for-particle-physicists-raulian-ionut-chiorescu-hannes-hansen-cern
- YouTube search: https://www.youtube.com/results?search_query=The+Shell+Awakens%3A+Cloud+Native+Workflows+for+Particle+Physicists+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2MU1de2B_C0
- YouTube title: The Shell Awakens: Cloud Native Workflows for Particle Ph... Raulian-Ionut Chiorescu & Hannes Hansen
- Match score: 0.839
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/the-shell-awakens-cloud-native-workflows-for-particle-physicists/2MU1de2B_C0.txt
- Transcript chars: 28332
- Keywords: running, gpu, actually, workloads, access, training, cluster, session, memory, cubeflow, machine, across, thanks, learning, platform, resources, latency, storage

### Resumo baseado na transcript

Welcome to our talk, The Shell Awakens, CloudNative Workflows for Particle Physicists. We are hosting the LHC, which is the so-called large headroom collider. Then someone else comes and says I need machine learning tooling to run distributed training across all the nodes that you have. So in order to cover all those use cases and all those requirements of our users, we had a look into the CNCF uh ecosystem and eventually we came up with this reference architecture that we actually released um a few days ago to the CNCF. So our platform is running on Kubernetes on a cluster with shared compute resources. So for machine learning we cover the whole MLOps life cycle using cubeflow ray kerf but we also offer interactive access to the system via ssh via jupyter notebooks or v code ides.

### Excerpt da transcript

Okay. Hello everyone. Welcome to our talk, The Shell Awakens, CloudNative Workflows for Particle Physicists. It's great to see so many faces in the auditorium. Um, yeah, my name is Hannes >> and I'm Raul. >> We are both computing engineers at CERN. CERN is the world's largest particle physics laboratory. We are hosting the LHC, which is the so-called large headroom collider. It's a 27 km ring below the French Alps where we accelerate protons to nearly the speed of light and then we let them collide and then we study what happens in this brief moment of time. When a machine is running it and runs for 24/7 and produces a lot of data. So the output is like in the range of terabytes per second and this is a little bit too much for us to handle. So in order to reduce a bit the data output we uh employ a so-called trigger chain which we use to filter out uninteresting data. And this whole chain consists of FPJAS but also CPUs and GPUs. And we recently started a R&D project which is called the next generation triggers where we try to employ like the latest machine learning research in this whole chain to support our users in this endeavor.

We run a platform for machine learning and scientific computing. And here on this picture you can actually see quite a real picture of a working environment at CERN. So you can see a bunch of physicists sitting in a uh oper control room operating the detector running some physics analysis and you can already see like everyone has like their own workflows their own requirements. So you can see oh maybe someone says oh I want to have an H100 GPU. Someone else might say I want to log into a shell. I need all my in like I need all my physics software pre-installed but I also want to install my own. Someone else might say I want to have a Jupyter notebook. Then someone else comes and says I need machine learning tooling to run distributed training across all the nodes that you have. And then someone else might want uh to run statistics on power consumption of his workloads. Okay. So in order to cover all those use cases and all those requirements of our users, we had a look into the CNCF uh ecosystem and eventually we came up with this reference architecture that we actually released um a few days ago to the CNCF.

You can check out the QR code here if you're interested. And the idea is uh quite straightforward. So our platform is running on Kubernetes on a cluster with shared compute resources. And then on top of that we have diff
