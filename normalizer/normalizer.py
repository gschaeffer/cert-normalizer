from .normalizer_base import NormalizerBase


class Normalizer(NormalizerBase):
    """
    Normalizer accepts raw data input from a certification certificate
    and attempts to transform (normalize) the data to correct atrributes.

    Args:
        **kwargs: dictionary with required values.
            job_id:         unique ID for tracing.
            raw_content:    Data content from certificate.
            members:        Members table name

    Returns:


    Raises:
        KeyError: Raises an exception.

    Example:
        n = normalizer.Normalizer(
            job_id=job_nbr,
            raw_content=raw_content,
            members=app.config.get("MEMBERS", []),
        )
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
