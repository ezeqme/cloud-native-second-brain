---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Christopher Nuland", "Hilliary Lipsig", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2CW7B/redefining-slis-for-llm-inference-managing-hybrid-cloud-with-vllm-llm-d-christopher-nuland-hilliary-lipsig-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Redefining+SLIs+for+LLM+Inference%3A+Managing+Hybrid+Cloud+with+vLLM+%26+LLM-D+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Redefining SLIs for LLM Inference: Managing Hybrid Cloud with vLLM & LLM-D - Christopher Nuland & Hilliary Lipsig, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Christopher Nuland, Hilliary Lipsig, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2CW7B/redefining-slis-for-llm-inference-managing-hybrid-cloud-with-vllm-llm-d-christopher-nuland-hilliary-lipsig-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Redefining+SLIs+for+LLM+Inference%3A+Managing+Hybrid+Cloud+with+vLLM+%26+LLM-D+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Redefining SLIs for LLM Inference: Managing Hybrid Cloud with vLLM & LLM-D.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW7B/redefining-slis-for-llm-inference-managing-hybrid-cloud-with-vllm-llm-d-christopher-nuland-hilliary-lipsig-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Redefining+SLIs+for+LLM+Inference%3A+Managing+Hybrid+Cloud+with+vLLM+%26+LLM-D+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BM4L74qL8zE
- YouTube title: Redefining SLIs for LLM Inference: Managing Hybrid Cloud wit... Christopher Nuland & Hilliary Lipsig
- Match score: 0.868
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/redefining-slis-for-llm-inference-managing-hybrid-cloud-with-vllm-llm/BM4L74qL8zE.txt
- Transcript chars: 28873
- Keywords: actually, llm, talking, models, looking, little, metrics, within, language, experience, seeing, batching, especially, gpu, similar, running, hillary, better

### Resumo baseado na transcript

I'm a technical marketing manager managing our um inference stack at Red Hat. I'm primarily involved in our VLLM and our LLMD uh projects and communities. And one commonality we're seeing is that S surres are having challenges adapting into this new paradigm. And this poses a lot of new challenges which we want to talk to you today about on how um there's a lot of actual metrics that will make it a lot easier for you to monitor these types of LLMs. um once you understand what those metrics are and what they're representing. So, when we talk about um like new metrics, right, we've said that a couple times.

### Excerpt da transcript

Good afternoon everyone. We're going to go ahead and get started. >> All right. Uh let me quickly introduce myself. My name is Christopher Nuland. I'm a technical marketing manager managing our um inference stack at Red Hat. I'm primarily involved in our VLLM and our LLMD uh projects and communities. >> My name is Hillary Lipig. I'm a senior principal site reliability engineer at Red Hat. Um I primarily work on something called Azure Red Hat Open Shift. Um, and then I also do anything else that seems kind of fun. Um, and and help Chris out with blogs and other such things here and there. >> So, today we're going to be talking about um how to redefine SLIS within the modern LL LLM based uh AI stack. Uh, you may have saw during the keynote something called LLMD, which is a project I'm heavily involved in. We'll talk a little bit about how that project kind of feeds into this conversation and then go over some of what some of these new metrics, SLI, SLAs's look like as we start creating new business objectives within our organization.

Uh, one thing I'm going to say real quick, I've been dealing with a GI issue uh for about 24 hours. I'm doing a lot better. But if I step up stage for a second and hand it over to Hillary, you'll know why or why I'm sipping ginger right now. Uh with that, let's just jump right in. So, uh one common thing that Hillary and I actually is kind of what brought us together here at Red Hat. Um one commonality we have is fencing. Um I did, uh Olympic fencing for a number of years as an EPA fencer. So I was in the junior Olympic circuit within the US. I did that from about late elementary school into college. And then if you want to go ahead and kind of explain your background, it's a little bit different than mine. It >> is background. So generally speaking, I have a background in in um athletics and martial arts. Um so I played soccer, I played water polo, I did karate and taekwond do. And then a few years ago I got into something called historical European martial arts. So if you see my long sword earrings, I am trained in German long sword techniques.

I have competed and I instruct or German long sword. Uh, historical European martial arts. I'm going to just really nerd dump on you real quick. You didn't ask for it, but you're welcome. Uh, is the historical predecessor to modern fencing and the manuals are from the late medieval, early renaissance period where dueling to the death was illegal and dueling to first blood was becoming
