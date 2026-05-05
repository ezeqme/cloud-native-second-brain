---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Application Development"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Paul Yu", "Sachi Desai", "Microsoft"]
sched_url: https://kccncna2025.sched.com/event/27FWo/rage-against-the-machine-fighting-ai-complexity-with-kubernetes-simplicity-paul-yu-sachi-desai-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Rage+Against+the+Machine%3A+Fighting+AI+Complexity+With+Kubernetes+Simplicity+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Rage Against the Machine: Fighting AI Complexity With Kubernetes Simplicity - Paul Yu & Sachi Desai, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Application Development]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Paul Yu, Sachi Desai, Microsoft
- Schedule: https://kccncna2025.sched.com/event/27FWo/rage-against-the-machine-fighting-ai-complexity-with-kubernetes-simplicity-paul-yu-sachi-desai-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Rage+Against+the+Machine%3A+Fighting+AI+Complexity+With+Kubernetes+Simplicity+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Rage Against the Machine: Fighting AI Complexity With Kubernetes Simplicity.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FWo/rage-against-the-machine-fighting-ai-complexity-with-kubernetes-simplicity-paul-yu-sachi-desai-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Rage+Against+the+Machine%3A+Fighting+AI+Complexity+With+Kubernetes+Simplicity+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RsROxLzsAe8
- YouTube title: Rage Against the Machine: Fighting AI Complexity With Kubernetes Simplicity - Paul Yu & Sachi Desai
- Match score: 0.961
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/rage-against-the-machine-fighting-ai-complexity-with-kubernetes-simpli/RsROxLzsAe8.txt
- Transcript chars: 22633
- Keywords: inference, application, actually, request, workspace, engine, gateway, basically, session, cubecon, information, schedule, endpoint, deploy, running, already, little, embedding

### Resumo baseado na transcript

So this session titled Rage Against the Machine, where we are fighting AI complexity with Kubernetes simplicity. It started off as a novelty toy that we were all having fun with, asking it silly questions, asking it to give us some funny jokes, maybe pirate jokes or Chuck Norris jokes or whatever. We could do that with fine-tuning, which is to run additional training on the models, but that could be costly and you might need an ML engineer to actually get it right. So that when a user makes an LLM request, relevant data is actually retrieved from the vector store, your original LLM query is then augmented and sent off to the LLM with better information to predict that next token, right? And when working with all of these um disjoint frameworks or tools, you can actually pull it together in a declarative mechanism on Kubernetes. So here we're going to talk about the CNCF sandbox project called the Kubernetes AI tool chain operator which we'll call Kaido.

### Excerpt da transcript

Hey everybody, welcome. This is the last session before the cube crawl, right? So Sachi and I, we are the last session before I guess free drinks. [laughter] Um, thanks for coming everybody. Is everybody having a great CubeCon? >> Woohoo. [cheering] Yeah. All right. So this session titled Rage Against the Machine, where we are fighting AI complexity with Kubernetes simplicity. And I'll start by just stating the obvious. AI is everywhere. It started off as a novelty toy that we were all having fun with, asking it silly questions, asking it to give us some funny jokes, maybe pirate jokes or Chuck Norris jokes or whatever. But at this point, we're at the period where we're starting to incorporate AI into our daily lives. And we've come to expect AI to give us relevant factual responses. And many AI enabled applications already do this and they do a pretty good job of it. But how can we all do this very easily? Well, that's the goal of this talk and that's to make LLMs more useful with Kubernetes. And I'm pretty sure we've all experienced this.

You ask AI a question and it gives you a wild answer and you're like say what? As awesome as AI is, there are times when you expect it to give you a factual real information answer, it just comes up short and it's a little overwhelming or underwhelming, I should say. And AI is great at making up stuff. It's what it's trained to do. It simply predicts what that next token should be. And sometimes that next sequence of tokens, they're just completely untrue. Take a look at this chat conversation that I had with the base model. I'm asking the model if there's any sessions at CubeCon North America where the session title includes Kao and Rag. Now, this model has some context and awareness of CubeCon. So, it at least knows that it should consult the CubeCon schedule for the information, but the URL is wrong and the answer is just flat out wrong. So, what can we do to give LLMs more context grounded with actual data to keep it from going off the rails? We could do that with fine-tuning, which is to run additional training on the models, but that could be costly and you might need an ML engineer to actually get it right.

And the most efficient way and especially if you're getting started is to implement a retrieval augmented generative or rag pipeline. With this setup, organizations can take knowledge bases, vectorize the data through an embedding model, and store them in a vector store. So that when a user makes an LLM requ
