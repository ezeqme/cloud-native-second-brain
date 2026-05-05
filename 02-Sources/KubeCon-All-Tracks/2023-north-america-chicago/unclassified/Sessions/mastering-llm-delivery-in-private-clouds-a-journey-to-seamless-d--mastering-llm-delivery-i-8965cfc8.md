---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Unclassified"
themes: ["AI ML", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Autumn Moulder", "Marwan Ahmed", "Cohere"]
sched_url: https://kccncna2023.sched.com/event/1R2qX/mastering-llm-delivery-in-private-clouds-a-journey-to-seamless-deployments-with-kubernetes-and-oci-autumn-moulder-marwan-ahmed-cohere
youtube_search_url: https://www.youtube.com/results?search_query=Mastering+LLM+Delivery+in+Private+Clouds%3A+A+Journey+to+Seamless+Deployments+with+Kubernetes+and+OCI+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Mastering LLM Delivery in Private Clouds: A Journey to Seamless Deployments with Kubernetes and OCI - Autumn Moulder & Marwan Ahmed, Cohere

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Autumn Moulder, Marwan Ahmed, Cohere
- Schedule: https://kccncna2023.sched.com/event/1R2qX/mastering-llm-delivery-in-private-clouds-a-journey-to-seamless-deployments-with-kubernetes-and-oci-autumn-moulder-marwan-ahmed-cohere
- Busca YouTube: https://www.youtube.com/results?search_query=Mastering+LLM+Delivery+in+Private+Clouds%3A+A+Journey+to+Seamless+Deployments+with+Kubernetes+and+OCI+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Mastering LLM Delivery in Private Clouds: A Journey to Seamless Deployments with Kubernetes and OCI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2qX/mastering-llm-delivery-in-private-clouds-a-journey-to-seamless-deployments-with-kubernetes-and-oci-autumn-moulder-marwan-ahmed-cohere
- YouTube search: https://www.youtube.com/results?search_query=Mastering+LLM+Delivery+in+Private+Clouds%3A+A+Journey+to+Seamless+Deployments+with+Kubernetes+and+OCI+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=y9lPk-oKZIA
- YouTube title: Mastering LLM Delivery in Private Clouds: A Journey to Seamless Dep... Autumn Moulder & Marwan Ahmed
- Match score: 0.809
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/mastering-llm-delivery-in-private-clouds-a-journey-to-seamless-deploym/y9lPk-oKZIA.txt
- Transcript chars: 40150
- Keywords: container, weights, challenges, artifact, download, storage, actually, running, gpu, solution, llm, private, models, dealing, registry, particular, specific, create

### Resumo baseado na transcript

thank you guys for joining uh we're here to talk about mastering llm delivery in private clouds a journey to seamless deployments mostly with kubernetes and oci and for those of you who are familiar with coh here we do have a relationship with another oci we're talking about open container initiative not Oracle Cloud infrastructure but hey our Oracle Cloud friends we we like you guys too so uh before we get started let me give you an intro so my name is Autumn Moulder I'm the director of

### Excerpt da transcript

thank you guys for joining uh we're here to talk about mastering llm delivery in private clouds a journey to seamless deployments mostly with kubernetes and oci and for those of you who are familiar with coh here we do have a relationship with another oci we're talking about open container initiative not Oracle Cloud infrastructure but hey our Oracle Cloud friends we we like you guys too so uh before we get started let me give you an intro so my name is Autumn Moulder I'm the director of infrastructure and security at cooh here we build large language models yes we put llm in the title of the talk mostly to just bring you all here uh I won't spoil what the talk actually is about but we will talk about LMS a little bit uh we build foundational models we help uh help companies that're looking to deploy and use this Tech in their Enterprise and then to talk us through some of the challenges we have hi everyone uh my name is Maran I am a member of technical staff coh here um previously I worked on the Azure kubernetes service team at Microsoft and more recently at the company formerly known as Twitter I've contributed to a lot of several cncf projects in the past so it's super exciting for me to see the foundational role cncf is doing with the success of the new kid on the Block large language models and we can't wait to share with you our journey so without further Ado I'll hand it back to Autumn all right thanks Marvin so I'll just tee this up a little bit uh before we get started i' like to know who I'm talking to so raise of hands who's a site reliability engineer or identifies as such okay we've got a few of you thank you one on the stage thank goodness uh data scientists ml's out there oh good number all right I have no idea what the rest of you are here for but I hope you find something valuable out of our conversation awesome so really briefly most of you probably know this because you saw the word llm in the talk of the title but what is a large language model um in a nutshell I asked our large language model this is what it is you know it's a way you can talk to computers uh with natural language um my favorite definition to be honest this one uh it's a pile of linear algebra on dis so for those of you who are infrastructure Engineers uh that's kind of relevant because we're just dealing with uh files right files on disk that store the the probabilities so we'll talk about the llm serving stack briefly just to Anchor this conversation and then uh and
