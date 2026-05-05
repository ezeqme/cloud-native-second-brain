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
speakers: ["Abdel Sghiouar", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2CW3q/optimizing-llm-inference-for-the-rest-of-us-abdel-sghiouar-google
youtube_search_url: https://www.youtube.com/results?search_query=Optimizing+LLM+Inference+for+the+Rest+of+Us+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Optimizing LLM Inference for the Rest of Us - Abdel Sghiouar, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Abdel Sghiouar, Google
- Schedule: https://kccnceu2026.sched.com/event/2CW3q/optimizing-llm-inference-for-the-rest-of-us-abdel-sghiouar-google
- Busca YouTube: https://www.youtube.com/results?search_query=Optimizing+LLM+Inference+for+the+Rest+of+Us+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Optimizing LLM Inference for the Rest of Us.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW3q/optimizing-llm-inference-for-the-rest-of-us-abdel-sghiouar-google
- YouTube search: https://www.youtube.com/results?search_query=Optimizing+LLM+Inference+for+the+Rest+of+Us+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xLum3amp6h0
- YouTube title: Optimizing LLM Inference for the Rest of Us - Abdel Sghiouar, Google
- Match score: 0.876
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/optimizing-llm-inference-for-the-rest-of-us/xLum3amp6h0.txt
- Transcript chars: 34664
- Keywords: actually, basically, particular, models, inference, request, server, running, trying, language, itself, container, single, accelerators, network, volume, extension, called

### Resumo baseado na transcript

Um, I was supposed to be giving this talk with my colleague Muffy, but unfortunately he's not here. Um, we did something similar at last CubeCon at London where we talked about basically running large language models on Kubernetes in general. You can do Kubernetes or you can use some sort of fully managed um um uh fully managed um uh platform, Bedrock, Azure, um Vert.exi, whatever. The only thing I would say probably is that if you are on the right side, the challenge you might be facing is the fact that most of these platforms does not scale to zero. Kubernetes is somewhere in the middle where you have kind of the benefit of the tweaking of your of your deployment however you want and then um you get all the the benefits of like you know securing optimizing etc etc. that you are using cannot actually fit your use case you need to twe it tweak it you need to tune it uh privacy is another one you just don't trust cloud cost uh cloud hosted models are usually super expensive per token and you

### Excerpt da transcript

Hi everyone, thank you for coming. Um, I was supposed to be giving this talk with my colleague Muffy, but unfortunately he's not here. Um, we did something similar at last CubeCon at London where we talked about basically running large language models on Kubernetes in general. And then we realized very quickly that we work for a big cloud provider and we have virtually unlimited access to GPUs which is not everybody's case. So we came up with this idea of like what what do you do if you're not the big cloud providers, right? So how do you optimize Kubernetes for running large language models, hence the title running open ALMs for the rest of us? My name is Abdel. I'm a developer advocate at Google. I work on Kubernetes. I co-host a podcast called Kubernetes podcast and I live up north in the cold country of Sweden. I want you to raise your hand if you have used either Ola before Docker model runner or hugging face to run a model. Oh, so that's most of you. So you can just leave. Thank you. I'm just kidding.

Um, what you have probably seen over time is that basically models are getting more and more sophisticated. And by sophisticated, they're just getting bigger and bigger. Both in terms of how many parameters they can actually support, which is how many neural networks inside the model, but also the size of the models themselves, right? And at some point you will get to a physical limitation of how many actually GPUs you will need to single to run a single model. and you will have to start thinking about running models across multiple GPUs or sometimes even running them across multiple hosts. So yeah, we're talking about cases where you're running DeepS at the 671 billion parameters which is a 1 roughly 1.3 terabyte model in the size if you have full quantization which is like the full precision of the model itself. Before I get going, I just want to spend like super quick time just doing some very basic explanations for concepts. I guess everybody knows what large language model. So I'm not going to spend time on that.

Inference is kind of this weird term that we use to describe a little bit of everything. Inference is essentially what happens when you give models data for the first time. So inference is what happens after training, right? So um inference is actually quite complex, quite more complex than people think about it because a lot of times when you run a model on your laptop and you just curl it, you think that that's inference. That's just y
