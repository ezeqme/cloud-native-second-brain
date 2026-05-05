---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Customizing + Extending Kubernetes"
themes: ["AI ML", "Runtime Containers", "Kubernetes Core", "SRE Reliability"]
speakers: ["Ritesh Naik", "MathWorks"]
sched_url: https://kccncna2021.sched.com/event/lV0Y/container-checkpointrestore-at-scale-for-fast-pod-startup-time-ritesh-naik-mathworks
youtube_search_url: https://www.youtube.com/results?search_query=Container+Checkpoint%2FRestore+at+Scale+for+Fast+Pod+Startup+Time+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Container Checkpoint/Restore at Scale for Fast Pod Startup Time - Ritesh Naik, MathWorks

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Los Angeles
- Speakers: Ritesh Naik, MathWorks
- Schedule: https://kccncna2021.sched.com/event/lV0Y/container-checkpointrestore-at-scale-for-fast-pod-startup-time-ritesh-naik-mathworks
- Busca YouTube: https://www.youtube.com/results?search_query=Container+Checkpoint%2FRestore+at+Scale+for+Fast+Pod+Startup+Time+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Container Checkpoint/Restore at Scale for Fast Pod Startup Time.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV0Y/container-checkpointrestore-at-scale-for-fast-pod-startup-time-ritesh-naik-mathworks
- YouTube search: https://www.youtube.com/results?search_query=Container+Checkpoint%2FRestore+at+Scale+for+Fast+Pod+Startup+Time+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BXVyszsbYmg
- YouTube title: Container Checkpoint/Restore at Scale for Fast Pod Startup Time - Ritesh Naik, MathWorks
- Match score: 0.931
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/container-checkpoint-restore-at-scale-for-fast-pod-startup-time/BXVyszsbYmg.txt
- Transcript chars: 22661
- Keywords: checkpoint, container, restore, application, runtime, running, seconds, containerized, initialization, around, startup, mathworks, couple, approach, available, support, vanilla, basically

### Resumo baseado na transcript

hello everyone and thank you for tuning in my name is ritesh naik and i'm here to talk about using container checkpoint restore in kubernetes to achieve fast port startup time we at mathworks have been using container checkpoint restore at high scale since 2016. and in this talk i'll go over how we incorporated checkpoint restore in kubernetes to achieve a scalable system hopefully you can take something away from the session and apply to your own environment on that note before we get started let me quickly introduce highly recommend enabling locks and metrics on checkpoint restore these locks and metrics are really helpful and at the same time maintainers are well accessible to discuss if you run into any issues i'll make this logs and metrics as easily as accessible as possible order to get all the required security patches updates and bug fixes there are some things to keep in mind about the limitations and boundaries of cryo in order to design checkpoint register around that for example one thing that comes to my mind is

### Excerpt da transcript

hello everyone and thank you for tuning in my name is ritesh naik and i'm here to talk about using container checkpoint restore in kubernetes to achieve fast port startup time we at mathworks have been using container checkpoint restore at high scale since 2016. and in this talk i'll go over how we incorporated checkpoint restore in kubernetes to achieve a scalable system hopefully you can take something away from the session and apply to your own environment on that note before we get started let me quickly introduce myself my name is ritesh naik and i'm a senior software engineer at mathworks for those who are not familiar with mathworks mathworks is a leading developer of mathematical computing software engineers scientists and researchers worldwide rely on its products to accelerate the pace of discovery innovation and development i've been at mathworks for over five years working on various areas of infrastructure and scalability my team and i have been focusing on doing things in kubernetes space since few years if you'd like to reach out to me after this talk feel free to ping me on kubernetes slack or via email i'm happy to talk about all things containers kubernetes checkpoint restore travel or anything for that matter so in this talk i'll go with the motivation behind using container checkpoint restore quick introduction of checkpoint restore along with a demo our solution of using container checkpoint restoring kubernetes along with some of the lessons learned best practices and future enhancements finally we'll wrap it up with q a at the end as in any typical kubernetes cluster here we have a workload of containerized applications orchestrated by kubernetes this workload could include application serving concurrent requests like web service or each request could be handled by individual containerized application like in a function as a service or serverless setup applications could come up pretty fast or they might have initialization overhead now keeping different workloads in mind what are some of the things we need to consider to build a scalable system first and foremost system should be able to react quickly and scale fast to any unexpected traffic spikes secondly there should not be any first use performance impact on the latency due to a cold start this is basically the time spent on setting up the container environment along with the application initialization to come up ready this could be avoided by keeping the containerized applicati
