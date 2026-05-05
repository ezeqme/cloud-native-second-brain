---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Keynote Sessions"
themes: ["AI ML", "Security"]
speakers: ["Jakub Suchy", "Director of Solutions Engineering", "HAProxy Technologies"]
sched_url: https://kccnceu2025.sched.com/event/1txCG/sponsored-keynote-lessons-learned-in-llm-prompt-security-jakub-suchy-director-of-solutions-engineering-haproxy-technologies
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Lessons+Learned+in+LLM+Prompt+Security+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Sponsored Keynote: Lessons Learned in LLM Prompt Security - Jakub Suchy, Director of Solutions Engineering, HAProxy Technologies

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United Kingdom / London
- Speakers: Jakub Suchy, Director of Solutions Engineering, HAProxy Technologies
- Schedule: https://kccnceu2025.sched.com/event/1txCG/sponsored-keynote-lessons-learned-in-llm-prompt-security-jakub-suchy-director-of-solutions-engineering-haproxy-technologies
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Lessons+Learned+in+LLM+Prompt+Security+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: Lessons Learned in LLM Prompt Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txCG/sponsored-keynote-lessons-learned-in-llm-prompt-security-jakub-suchy-director-of-solutions-engineering-haproxy-technologies
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Lessons+Learned+in+LLM+Prompt+Security+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UI-b-Odg39A
- YouTube title: Sponsored Keynote: Lessons Learned in LLM Prompt Security - Jakub Suchy
- Match score: 0.983
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/sponsored-keynote-lessons-learned-in-llm-prompt-security/UI-b-Odg39A.txt
- Transcript chars: 4735
- Keywords: security, gateway, prompt, balancer, ultimately, models, llm, everybody, inference, classification, instance, tokens, filter, keynote, lessons, learned, previous, engine

### Resumo baseado na transcript

You might know of us as the company behind Harroxy, the legendary opensource software load balancer that a lot of you are probably using. Today I'm going to be piggybacking on the previous keynote about performance and security and LLMs because I think there are a lot of topics we should talk about. So we're going to add prompt security to the AI gateway and basically run the model itself in the AI gateway. The only problem is if you make a typo in the filter or in your text, the text filter will no longer work while the LLM will interpret it correctly. And three, I think that the AI gateways are necessary, but the security is is evolving. In the end, as I said, I think we're in the 2003 of OAS top 10 right now in AI security.

### Excerpt da transcript

Hello everybody. My name is Jacob and I work at Haroxy Technologies. You might know of us as the company behind Harroxy, the legendary opensource software load balancer that a lot of you are probably using. Today I'm going to be piggybacking on the previous keynote about performance and security and LLMs because I think there are a lot of topics we should talk about. I talked to a lot of our customers and they all say we're all in on AI, but I think the risks of that are yet to be understood. I think we're kind of in the 2003 of OASP top 10 for web security right now in terms of LLM security. So when they talk about I'm being allin on AI security or an AI, the first step they usually think about is well we're going to build an AI gateway. And so what's an AI gateway? Well, it's an API gateway, right? We've all built one at this point or most of the projects in load balancers have built one API gateway right now, an AI gateway. So, we're going to do some authentication. We're going to do raid limiting.

We're going to do PII detection or maybe PII extraction and prompt routing before we send the data to an inference engine, which is ultimately an HTTP API. But I think one of the things that's missing there or possibly missing is prompt security. And that's really, you know, the ignore all previous instructions that doesn't work anymore or a time bandit attack that used to work with open AI until recently. So there are obviously solutions to that. For example, there's a prompt guard model and a llama guard model from meta. There's a shield gemma from Google. And in the end, many of these are built on some kind of a variation of dberta classification. It's a set of models. So they are actually large language models that are classifying. You ask, is this prompt safe? Yes or no? And they answer yes or no. So it's ultimately classification problem. So we're going to add prompt security to the AI gateway and basically run the model itself in the AI gateway. Um, so I did that and I ran these models inside an AI gateway inside a load balancer and ultimately what I found and this is what I want to talk about is it's pretty slow.

So if you run a model like this on a G6X large AWS instance, which is ultimately a pretty big instance at this point, if you start approaching 500 tokens, it takes somewhere between 150 to 200 milliseconds to process the prompt. And most prompts are bigger and most of these models have a context window of about 500 tokens. So if your prompt
