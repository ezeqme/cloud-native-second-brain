---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Vikram Venkataraman", "AWS", "Srikanth Rajan", "Salesforce"]
sched_url: https://kccncna2025.sched.com/event/27FVk/1000-clusters-1-brain-salesforces-approach-to-self-healing-using-aiops-vikram-venkataraman-aws-srikanth-rajan-salesforce
youtube_search_url: https://www.youtube.com/results?search_query=1000+Clusters%2C+1+Brain%3A+Salesforce%E2%80%99s+Approach+To+Self-Healing+Using+AIOps+CNCF+KubeCon+2025
slides: []
status: parsed
---

# 1000 Clusters, 1 Brain: Salesforce’s Approach To Self-Healing Using AIOps - Vikram Venkataraman, AWS & Srikanth Rajan, Salesforce

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Vikram Venkataraman, AWS, Srikanth Rajan, Salesforce
- Schedule: https://kccncna2025.sched.com/event/27FVk/1000-clusters-1-brain-salesforces-approach-to-self-healing-using-aiops-vikram-venkataraman-aws-srikanth-rajan-salesforce
- Busca YouTube: https://www.youtube.com/results?search_query=1000+Clusters%2C+1+Brain%3A+Salesforce%E2%80%99s+Approach+To+Self-Healing+Using+AIOps+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre 1000 Clusters, 1 Brain: Salesforce’s Approach To Self-Healing Using AIOps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVk/1000-clusters-1-brain-salesforces-approach-to-self-healing-using-aiops-vikram-venkataraman-aws-srikanth-rajan-salesforce
- YouTube search: https://www.youtube.com/results?search_query=1000+Clusters%2C+1+Brain%3A+Salesforce%E2%80%99s+Approach+To+Self-Healing+Using+AIOps+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Y29VmBH-HA8
- YouTube title: 1000 Clusters, 1 Brain: Salesforce’s Approach To Self-Healin... Vikram Venkataraman & Srikanth Rajan
- Match score: 0.858
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/1000-clusters-1-brain-salesforces-approach-to-self-healing-using-aiops/Y29VmBH-HA8.txt
- Transcript chars: 32507
- Keywords: agents, engineers, infrastructure, operations, platform, clusters, engineer, application, provide, troubleshooting, metrics, identify, cluster, remediation, actions, events, problems, salesforce

### Resumo baseado na transcript

Bad news, getting paged at 3:00 a.m., going through your alert storms, troubleshooting 5 hours for a 5-minute fix, it's not going to go away. But the good news is that if you can build an intelligent system that can correlate the telemetry signals that can help us make the decisions faster and that's where we believe AI ops can help us. probably he may have to go through you know 50,000 time series of metrics two pabytes of logs and he's already raising against the time. First thing is isolating the noise from the actual information or the actual problem. He has to swam through them and identify the one that matters the most getting to have all the information that flows across your complex architecture because many of times it's not that application. So you must have all the informations as your request flows through your complex architecture.

### Excerpt da transcript

All right, thank you so much for joining us. Uh, have some good news and bad news. Bad news, getting paged at 3:00 a.m., going through your alert storms, troubleshooting 5 hours for a 5-minute fix, it's not going to go away. But the good news is that if you can build an intelligent system that can correlate the telemetry signals that can help us make the decisions faster and that's where we believe AI ops can help us. That's going to be the focus of today's session. My name is Vikramatraan. I'm a solutions architect at AWS. I work with some of our strategic customers that operate Kubernetes at large scale. Any platform engineers, SR in the house? You have my respect folks. Well, uh, okay, let me ask the this question as well. Uh, how many of you here operate more than 50 Kubernetes clusters? Keep your hands raised if you're operating more than 100, 500, thousand. Okay, not a lot of you, but I hope we can take some of what you learned today, convince an R and do this P on the AI ops framework and help manage Kubernetes, you know, in an intelligent way.

I would say uh that said, I'm a big fan of analogies. I wanted to emphasize on the challenges and the know nightmare of managing Kubernetes clusters at large scale. So, I I came up with this the inter interstate 75. Um, now if the data is correct, the Interstate 75 is the third busiest interstate in the whole of the United States. Imagine putting yourself sitting at the traffic control center. You would want to make sure the traffic flows smooth. There is constant movement of vehicles in and out of the city. There's crashes, weather impingments, you name it. You got all the challenges. Sounds challenging, right? Just multiply this chaos by 10 more interstates. And that's exactly what we mean when we say managing thousand Kubernetes clusters feels like. Uh a disclaimer, this is yes a session on AI, but the slides are not generated by AI except for these images. But that said, it's all like generated by myself. Now looking from the lens of an on call engineer who wakes up at 3:00 a.m. and he finds there are like 10,000 alerts waiting to be attended.

probably he may have to go through you know 50,000 time series of metrics two pabytes of logs and he's already raising against the time. Do you think this is a monitoring challenge? No. It's an intelligent crisis right the lack of um you know correlating the telemetry signals and where a five minute like fix takes 5 hours for you to troubleshoot that tells us ther
