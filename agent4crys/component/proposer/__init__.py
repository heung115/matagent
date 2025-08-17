from .gpt import OAProposer
from .planner import Planner

# from .claude import ClaudeProposer


def load_proposer(args, target_prompt, knowledge_base):
    llm_model = args.llm_model
    base_url = getattr(args, "base_url", None)

    if llm_model == "gpt-4o":
        model_id = "gpt-4o-2024-08-06"
        proposer = OAProposer(
            target_val=args.target_value,
            target_prompt=target_prompt,
            knowledge_base=knowledge_base,
            gpt_model=model_id,
            base_url=base_url,
        )
        if args.use_planning:
            return Planner(proposer)
        else:
            return proposer
    elif llm_model == "o1":
        model_id = "o1-2024-12-17"
        proposer = OAProposer(
            target_val=args.target_value,
            target_prompt=target_prompt,
            knowledge_base=knowledge_base,
            gpt_model=model_id,
            base_url=base_url,
        )
        if args.use_planning:
            return Planner(proposer)
        else:
            return proposer
    elif llm_model == "o3-mini":
        model_id = "o3-mini-2025-01-31"
        proposer = OAProposer(
            target_val=args.target_value,
            target_prompt=target_prompt,
            knowledge_base=knowledge_base,
            gpt_model=model_id,
            base_url=base_url,
        )
        if args.use_planning:
            return Planner(proposer)
        else:
            return proposer
    elif llm_model == "gpt-3.5-turbo":
        model_id = "gpt-3.5-turbo-0125"
        proposer = OAProposer(
            target_val=args.target_value,
            target_prompt=target_prompt,
            knowledge_base=knowledge_base,
            gpt_model=model_id,
            base_url=base_url,
        )
        if args.use_planning:
            return Planner(proposer)
        else:
            return proposer
    # 로컬 모델 지원
    elif llm_model in [
        "llama3.2",
        "llama3.1",
        "llama2",
        "mistral",
        "codellama",
        "qwen",
        "gemma",
        "gpt-oss:20b",
        "gpt-oss",
    ]:
        # Ollama 모델명으로 사용
        proposer = OAProposer(
            target_val=args.target_value,
            target_prompt=target_prompt,
            knowledge_base=knowledge_base,
            gpt_model=llm_model,
            base_url=base_url or "http://localhost:11434/v1",
        )
        if args.use_planning:
            return Planner(proposer)
        else:
            return proposer
    # elif llm_model == "claude-3-5":
    #     model_id = "claude-3-5-sonnet-20241022"
    #     proposer = ClaudeProposer(
    #         target_val=args.target_value,
    #         target_prompt=target_prompt,
    #         knowledge_base=knowledge_base,
    #         claude_model=model_id,
    #     )
    #     if args.use_planning:
    #         return Planner(proposer)
    #     else:
    #         return proposer
    else:
        raise ValueError(f"Model {llm_model} not supported")
