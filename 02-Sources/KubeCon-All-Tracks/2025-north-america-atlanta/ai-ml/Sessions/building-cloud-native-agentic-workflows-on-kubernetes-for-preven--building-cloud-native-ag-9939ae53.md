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
speakers: ["Benjamin Consolvo", "AMD", "Daron Yöndem", "AWS"]
sched_url: https://kccncna2025.sched.com/event/27Fcx/building-cloud-native-agentic-workflows-on-kubernetes-for-preventative-healthcare-benjamin-consolvo-amd-daron-yondem-aws
youtube_search_url: https://www.youtube.com/results?search_query=Building+Cloud+Native+Agentic+Workflows+on+Kubernetes+for+Preventative+Healthcare+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Building Cloud Native Agentic Workflows on Kubernetes for Preventative Healthcare - Benjamin Consolvo, AMD & Daron Yöndem, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Benjamin Consolvo, AMD, Daron Yöndem, AWS
- Schedule: https://kccncna2025.sched.com/event/27Fcx/building-cloud-native-agentic-workflows-on-kubernetes-for-preventative-healthcare-benjamin-consolvo-amd-daron-yondem-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Cloud+Native+Agentic+Workflows+on+Kubernetes+for+Preventative+Healthcare+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Building Cloud Native Agentic Workflows on Kubernetes for Preventative Healthcare.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fcx/building-cloud-native-agentic-workflows-on-kubernetes-for-preventative-healthcare-benjamin-consolvo-amd-daron-yondem-aws
- YouTube search: https://www.youtube.com/results?search_query=Building+Cloud+Native+Agentic+Workflows+on+Kubernetes+for+Preventative+Healthcare+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HYgxGUrdtik
- YouTube title: Building Cloud Native Agentic Workflows on Kubernetes for Preven... Benjamin Consolvo & Daron Yöndem
- Match score: 0.887
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/building-cloud-native-agentic-workflows-on-kubernetes-for-preventative/HYgxGUrdtik.txt
- Transcript chars: 18479
- Keywords: deployment, healthcare, cluster, hardware, source, command, prometheus, inference, application, models, preventative, patients, patient, emails, actually, hugging, dashboard, cloudnative

### Resumo baseado na transcript

So unfortunately Darren's not able to join me today, but I'm happy to to give you this talk and show you some of the internal workings of a cloudnative preventive healthcare system. So all the way from the hardware to the model deployment, the infrastructure, and then to a front-end UI. Um the orchestration is done with um Kubernetes and Helmcharts for declarative deployment and API 6 provides the API gateway authentication traffic management. Uh Prometheus monitors all the inference endpoints and then Graphana pulls that data from Prometheus for monitoring. So the main components of the deployment bashcript are setting up the Kubernetes cluster and the config, the engineext controller as the foundation to API 6 uh keycloak and uh API 6 setup with anible and then uh using VLM for uh inference for the for the LLMs and then observability with Prometheus and Graphfana. So after declaring some of those administrative variables um we are uh looking at you know on the at the bottom of that script deploy Kubernetes fresh on so deploying the Kubernetes server the engineext controller uh the keycloak for authentication API 6 API gateway

### Excerpt da transcript

Welcome everyone. My name is Ben Consalo and I'm an AI engineer at AMD. So unfortunately Darren's not able to join me today, but I'm happy to to give you this talk and show you some of the internal workings of a cloudnative preventive healthcare system. So all the way from the hardware to the model deployment, the infrastructure, and then to a front-end UI. So, if you're thinking of taking notes, uh, just know that all these slides are posted on the sketch.com website. Um, so, you know, if you want if you want to stick around and ask questions afterward, that's that's great. But, um, feel free to use those slides, the PDF of these slides on there. And also stick around to the end of the talk because I have, uh, some free AMD cloud credits for our GPUs. So, you can take advantage of that. So healthcare organizations need to reach thousands of patients for preventative screenings. Uh but manual outreach often doesn't scale and automate automation lacks personalization sometimes. And so the solution that uh I built was building an agentic AI system to generate patient specific criteria with the help of a screening prompt.

typing in um a prompt and and then looking at a patient database uh and ultimately to write these um outreach emails to suggest to patients that they schedule a screening. So here I'm using a cloudnative stack to build the backend model deployment uh that's secure and can sit on uh the hardware of your choosing whether you have like an on-prem cluster or you want to uh deploy it on the cloud either way it sits on your own infrastructure and all the services would sit there. So um this I want to go over the the hardware stack uh so or sorry the the full software and hardware stack. Uh so from hardware to healthcare the the software stack is entirely open source. Uh the hardware that I tested was the AMD Epic CPUs, Intel Xeon CPUs and Intel Gaudy accelerators. Um the orchestration is done with um Kubernetes and Helmcharts for declarative deployment and API 6 provides the API gateway authentication traffic management. Uh Prometheus monitors all the inference endpoints and then Graphana pulls that data from Prometheus for monitoring.

And then Autogen is a Microsoft open source framework uh that's for Agentic AI if you're not familiar with it and it's it's what's used to define the actual screening criteria filter the patient records and generate those personalized emails. And then finally on the front end is a Streamlit application hosted on H
