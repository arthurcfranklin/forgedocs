"""Exceções customizadas do ForgeDocs."""


class ForgeDocsError(Exception):
    """Classe base para todas as exceções controladas do ForgeDocs."""


class ConfigurationError(ForgeDocsError):
    """Erro relacionado às configurações da aplicação."""


class FileValidationError(ForgeDocsError):
    """Erro durante a validação de arquivos."""


class UnsupportedFormatError(ForgeDocsError):
    """Formato de arquivo não suportado."""


class ConversionError(ForgeDocsError):
    """Erro ocorrido durante uma conversão de documentos."""


class OutputDirectoryError(ForgeDocsError):
    """Erro relacionado ao diretório de saída."""


class TemporaryDirectoryError(ForgeDocsError):
    """Erro relacionado aos arquivos temporários."""